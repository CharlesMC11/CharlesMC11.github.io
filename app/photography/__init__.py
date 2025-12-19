"""Package for working with the photography pages"""

__author__ = "Charles Mesa Cayobit"

from flask import Blueprint, render_template

from ..auth import check_authentication, require_authentication

bp = Blueprint(
    "photography",
    __name__,
    template_folder="templates",
    url_prefix="/photo",
)

bp.before_request(check_authentication)


@bp.get("/")
def view() -> str:
    return render_template("photography/all.html")


@bp.get("/personal")
def personal() -> str:
    return render_template("photography/personal.html")


@bp.get("/events")
@require_authentication
def events() -> str:
    return render_template("photography/events.html")
