from flask import Blueprint, render_template

bp = Blueprint("3d", __name__, template_folder="templates", url_prefix="/3d")


@bp.get("/")
def view() -> str:
    return render_template("3d/all.html")


@bp.get("/re-connection")
def re_connection() -> str:
    return render_template("3d/re-connection.html")


@bp.get("/a-trace")
def a_trace() -> str:
    return render_template("3d/a-trace.html")


@bp.get("/kikis-bakery")
def kikis_bakery() -> str:
    return render_template("3d/kikis-bakery.html")


@bp.get("/jet-jacked")
def jet_jacked() -> str:
    return render_template("3d/jet-jacked.html")
