import sys
from datetime import date
from pathlib import Path
from typing import Any

import minify_html
import yaml
from jinja2 import Environment, FileSystemLoader

SRC_DIR = Path(__file__).parent
TEMPLATE_DIR = SRC_DIR / "templates"
CONTENT_DIR = SRC_DIR.parent / "content"

BUILD_DIR = SRC_DIR.parent / "build"
BUILD_DIR.mkdir(parents=True, exist_ok=True)

ENV = Environment(
    trim_blocks=True, lstrip_blocks=True, loader=FileSystemLoader(TEMPLATE_DIR)
)


YEAR = date.today().year

# Public functions


def render_template() -> None:
    """Render a template whose filename is given at the CLI.

    Expects `sys.argv[1]` to be the filename of the template to render.
    """

    filename = Path(sys.argv[1])
    content = ENV.get_template(str(filename)).render(
        year=YEAR, socials=SOCIALS
    )
    (BUILD_DIR / filename.stem).write_text(_minify(content))


def render_cv() -> None:
    """Render the CV page."""

    content = ENV.get_template("cv/all.html.jinja").render(
        year=YEAR,
        experience=_experience(),
        projects=_load_sorted_yaml("projects.yaml"),
        skills=_load_yaml("skills.yaml"),
        education=_load_sorted_yaml("education.yaml"),
        socials=SOCIALS,
    )
    (BUILD_DIR / "cv.html").write_text(_minify(content))


# Protected helpers


def _experience() -> list[dict[str, Any]]:
    """Parse `experience.yaml` into a list of dictionaries."""

    content = _load_yaml("experience.yaml")
    for company in content:
        company["roles"].sort(key=_by_end_date, reverse=True)
    content.sort(key=lambda x: _by_end_date(x["roles"][0]), reverse=True)

    return content


def _by_end_date(entry: dict[str, date | Any]) -> tuple[date, date]:
    """Get the end date and start date for a given entry.

    :param entry: entry from a dictionary entry from a YAML file.

    :returns: A tuple containing the end and start dates of an entry.
    """

    return entry.get("end_date", date.max), entry["start_date"]


def _load_sorted_yaml(
    filename: str, key=_by_end_date
) -> list[dict[str, date | Any]]:
    """Parse a YAML file into a sorted list of dictionaries."""

    content = _load_yaml(filename)
    content.sort(key=key, reverse=True)

    return content


def _load_yaml(filename: str) -> list[dict[str, Any]] | dict[str, Any]:
    with (CONTENT_DIR / filename).open() as f:
        return yaml.safe_load(f)


def _date_filter(entry: date) -> str:
    """Date format filter for Jinja."""

    return entry.strftime("%b %Y")


def _minify(content: str) -> str:
    return minify_html.minify(content, minify_css=True, minify_js=True)


ENV.filters["date"] = _date_filter

SOCIALS = _load_yaml("socials.yaml")
