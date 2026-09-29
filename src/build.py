import sys
from datetime import date
from pathlib import Path

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
    """Render a template whose filename is given at the CLI."""

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


def _experience() -> list[dict]:
    content = _load_yaml("experience.yaml")
    for company in content:
        company["roles"].sort(key=_sort_by_date, reverse=True)
    content.sort(key=lambda x: _sort_by_date(x["roles"][0]), reverse=True)

    return content


def _load_sorted_yaml(filename: str) -> list[dict]:
    content = _load_yaml(filename)
    content.sort(key=_sort_by_date, reverse=True)

    return content


def _load_yaml(filename: str) -> list[dict] | dict:
    with (CONTENT_DIR / filename).open() as f:
        return yaml.safe_load(f)


def _sort_by_date(entry: dict) -> tuple[date, date]:
    return entry.get("end_date", date.max), entry["start_date"]


def _format_date(entry: date) -> str:
    return entry.strftime("%b %Y")


def _minify(content: str) -> str:
    return minify_html.minify(content, minify_css=True, minify_js=True)


ENV.filters["date"] = _format_date

SOCIALS = _load_yaml("socials.yaml")
