import os
import re
from collections.abc import Callable
from datetime import datetime, timedelta
from functools import wraps
from time import time

from flask import (
    Blueprint,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

URL_PATTERN = re.compile(r"https?://.+/(.+?)")


bp = Blueprint(
    "auth", __name__, template_folder="templates", url_prefix="/auth"
)


def check_authentication() -> None:
    """Check if the user is authenticated."""

    redirect_url = request.url
    is_authenticated = session.get(f"auth_? {redirect_url}", False)
    authentication_time = session.get(f"auth_t {redirect_url}", 0)

    if is_authenticated and authentication_time > 0:
        time_delta = datetime.now() - datetime.fromtimestamp(
            float(authentication_time)
        )
        if time_delta > timedelta(seconds=30):
            is_authenticated = False

    g.is_authenticated = is_authenticated and authentication_time > 0


def require_authentication(original_view: Callable) -> Callable:
    """Decorator for redirecting to the authentication page if needed."""

    @wraps(original_view)
    def wrapped_view(*args, **kwargs):
        if not g.is_authenticated:
            session["redirect"] = request.url

            return redirect(url_for("auth.view"))

        return original_view(*args, **kwargs)

    return wrapped_view


@bp.route("", methods=["GET", "POST"])
def view():
    if request.method == "POST":
        redirect_url = session.get("redirect", "")
        redirect_path = URL_PATTERN.fullmatch(redirect_url)[1]

        if request.form.get("password") == os.getenv(
            f"PASSWORD_{redirect_path.upper()}"
        ):
            session[f"auth_? {redirect_url}"] = True
            session[f"auth_t {redirect_url}"] = time()

            if redirect_url:
                return redirect(redirect_url)

        return redirect(url_for("index"))

    return render_template("auth/auth.html")
