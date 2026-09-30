import sys
from collections.abc import Sequence
from datetime import date
from pathlib import Path
from typing import Any

import minify_html
import rcssmin
import yaml
from coloraide import Color
from jinja2 import Environment, FileSystemLoader

SRC_DIR = Path(__file__).parent
TEMPLATE_DIR = SRC_DIR / "templates"
CONTENT_DIR = SRC_DIR.parent / "content"

BUILD_DIR = SRC_DIR.parent / "build"
BUILD_DIR.mkdir(parents=True, exist_ok=True)

JINJA_ENV = Environment(
    trim_blocks=True,
    lstrip_blocks=True,
    loader=FileSystemLoader((TEMPLATE_DIR, STATIC_DIR)),
)


CURRENT_YEAR = date.today().year

# Public functions


def build_page() -> None:
    """Render and compile a page template passed via CLI argument.

    Expects `sys.argv[1]` to be the filename of the template to render.
    """

    template_name = Path(sys.argv[1]).name
    content = JINJA_ENV.get_template(template_name).render(
        socials=SOCIALS, current_year=CURRENT_YEAR
    )
    (BUILD_DIR / template_name.removesuffix(".jinja")).write_text(
        _minify(content)
    )


def build_cv() -> None:
    """Aggregate the CV data sources and compile the unified CV page."""

    content = JINJA_ENV.get_template("cv/all.html.jinja").render(
        socials=SOCIALS,
        experience=_load_and_sort_experience(),
        projects=_load_and_sort_yaml("projects.yaml"),
        skills=_load_yaml("skills.yaml"),
        education=_load_and_sort_education(),
        current_year=CURRENT_YEAR,
    )
    (BUILD_DIR / "cv.html").write_text(_minify(content))


def build_css() -> None:

    raw_colors = _load_yaml("colors.yaml")

    processed_colors = _build_colors(
        raw_colors["space"],
        raw_colors["primary_color"],
        raw_colors["secondary_color"],
        raw_colors["tertiary_color"],
    )
    css_strings = {k: v.to_string() for k, v in processed_colors.items()}

    content = JINJA_ENV.get_template("style.css.jinja").render(**css_strings)
    (BUILD_DIR / "style.css").write_text(
        rcssmin.cssmin(content, keep_bang_comments=False), encoding="utf-8"
    )


# Protected helpers


def _load_and_sort_experience() -> list[dict[str, Any]]:
    """Parse `experience.yaml` into a list of dictionaries."""

    content = _load_yaml("experience.yaml")
    for company in content:
        company["roles"].sort(key=_record_date_key, reverse=True)
    content.sort(key=lambda x: _record_date_key(x["roles"][0]), reverse=True)

    return content


def _load_and_sort_education() -> list[dict[str, Any]]:
    """Parse `education.yaml` into a list of dictionaries."""

    content = _load_yaml("education.yaml")
    for institution in content:
        concentrations = institution["concentrations"]

        concentrations.sort(
            key=lambda x: (x["award_date"], institution["start_date"]),
            reverse=True,
        )
    content.sort(
        key=lambda x: x["concentrations"][0]["award_date"], reverse=True
    )

    return content


def _build_colors(
    color_space: str,
    primary_coords: Sequence[int | float],
    secondary_coords: Sequence[int | float],
    tertiary_coords: Sequence[int | float],
) -> dict[str, Color]:

    primary = Color(color_space, primary_coords)

    primary_dark = primary.clone()
    primary_dark["l"] /= 1.25

    primary_light = primary.clone()
    primary_light["l"] *= 3

    primary_transparent = primary.clone()
    primary_transparent["alpha"] = 0.75

    secondary = Color(color_space, secondary_coords)

    secondary_dark = secondary.clone()
    secondary_dark["l"] = 0.95

    tertiary = Color(color_space, tertiary_coords)

    tertiary_light = tertiary.clone()
    tertiary_light["s"] /= 3
    tertiary_light["l"] = 0.95

    return {
        "primary_color": primary,
        "primary_dark": primary_dark,
        "primary_light": primary_light,
        "primary_transparent": primary_transparent,
        "secondary_color": secondary,
        "secondary_dark": secondary_dark,
        "tertiary_color": tertiary,
        "tertiary_light": tertiary_light,
    }


def _record_date_key(record: dict[str, date | Any]) -> tuple[date, date]:
    """Get the end date and start date for a given val.

    :param record: A record from a YAML file.

    :returns: A tuple containing the end and start dates of a record.
    """

    return record.get("end_date", date.max), record["start_date"]


def _load_and_sort_yaml(
    filename: str, key=_record_date_key
) -> list[dict[str, date | Any]]:
    """Parse a YAML file into a sorted list of dictionaries."""

    content = _load_yaml(filename)
    content.sort(key=key, reverse=True)

    return content


def _load_yaml(filename: str) -> list[dict[str, Any]] | dict[str, Any]:
    with (CONTENT_DIR / filename).open() as f:
        return yaml.safe_load(f)


def _date_formatter(val: date) -> str:
    """Date format filter for Jinja."""

    return val.strftime("%b %Y")


def _minify(content: str) -> str:
    return minify_html.minify(content, minify_css=True, minify_js=True)


JINJA_ENV.filters["date_fmt"] = _date_formatter

SOCIALS = _load_yaml("socials.yaml")
