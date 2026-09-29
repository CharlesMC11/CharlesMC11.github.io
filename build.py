from datetime import date
from pathlib import Path

import minify_html
import yaml
from jinja2 import Environment, FileSystemLoader

# Public functions

SRC_DIR = Path(__file__).parent
TEMPLATE_DIR = SRC_DIR / "templates"
CONTENT_DIR = SRC_DIR / "content"

BUILD_DIR = SRC_DIR / "build"

ENV = Environment(
    trim_blocks=True, lstrip_blocks=True, loader=FileSystemLoader(TEMPLATE_DIR)
)


# Public function


def main() -> None:
    render("index.html")
    render("about-me.html")

    render_cv()


# Protected helpers


def render(filename: str) -> None:
    template = ENV.get_template(filename + ".jinja")
    content = template.render()
    content = minify(content)

    (BUILD_DIR / filename).write_text(content)


def minify(content: str) -> str:
    return minify_html.minify(content, minify_css=True, minify_js=True)


def render_cv() -> None:
    template = ENV.get_template("cv/all.html.jinja")

    content = template.render(
        experience=experience(),
        projects=load_data("projects.yaml"),
        skills=load_yaml("skills.yaml"),
        education=load_data("education.yaml"),
    )
    content = minify(content)

    (BUILD_DIR / "cv.html").write_text(content)


def experience() -> list[dict]:
    content = load_yaml("experience.yaml")
    for company in content:
        company["roles"].sort(key=_sort_by_date, reverse=True)
    content.sort(key=lambda x: _sort_by_date(x["roles"][0]), reverse=True)

    return content


def load_data(filename: str) -> list[dict]:
    content = load_yaml(filename)
    content.sort(key=_sort_by_date, reverse=True)

    return content


def load_yaml(filename: str) -> list[dict] | dict:
    with (CONTENT_DIR / filename).open() as f:
        return yaml.safe_load(f)


def _sort_by_date(entry: dict) -> tuple[date, date]:
    return entry.get("end_date", date.max), entry["start_date"]


if __name__ == "__main__":
    main()
