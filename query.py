import datetime
import os
import sqlite3
from typing import Any


def decode_date(value: bytes) -> str:
    """
    :param value: The date in ISO format
    :return: `Present` or `MMM ’YY` where `MMM` is the 3-letter abbreviation of the month
    """

    decoded_value = value.decode("utf-8")
    if decoded_value == "9999-12-31":
        return "Present"
    return datetime.date.fromisoformat(decoded_value).strftime("%b ’%y")


sqlite3.register_converter("date", decode_date)


class SQLQueryHandler:
    root = None

    @classmethod
    def set_root(cls, root):
        if not os.path.exists(root):
            raise FileNotFoundError(root)

        cls.root = root

    def __init__(self, filename: str, root_dir: str | None = None) -> None:
        self._root_dir = root_dir or self.root
        self._filename = filename

        self._path = os.path.join(self._root_dir, filename)
        self._file = None

    def __enter__(self):
        ret = open(self._path, "rt", encoding="utf-8")
        self._file = ret

        return ret.read()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()

    @property
    def root_dir(self) -> str:
        return self._root_dir

    @property
    def filename(self) -> str:
        return self._filename

    @property
    def path(self) -> str:
        return self._path


SQLQueryHandler.set_root("sql")


def query_experience(cursor: sqlite3.Cursor, sql: str) -> Any:
    result: dict[str, Any] = {}

    query = cursor.execute(sql).fetchall()
    for employer, *job_details in query:
        if employer not in result:
            result[employer] = {}

        job_title, start_date, end_date, highlights = job_details
        if job_title not in result[employer]:
            result[employer][job_title] = {
                "start_date": start_date,
                "end_date": end_date,
            }

        if not highlights:
            continue

        if "highlights" not in result[employer][job_title]:
            result[employer][job_title]["highlights"] = []

        result[employer][job_title]["highlights"].append(highlights)

    return result


def query_projects(cursor: sqlite3.Cursor, sql: str) -> Any:
    result: dict[str, Any] = {}

    query = cursor.execute(sql).fetchall()
    for project, project_type, url, *project_details in query:
        if project not in result:
            result[project] = {"type": project_type, "url": url, "roles": {}}

        roles, start_date, end_date, highlights = project_details
        if roles not in result[project]["roles"]:
            result[project]["roles"][roles] = {
                "start_date": start_date,
                "end_date": end_date,
            }

        if not highlights:
            continue

        if "highlights" not in result[project]["roles"][roles]:
            result[project]["roles"][roles]["highlights"] = []

        result[project]["roles"][roles]["highlights"].append(highlights)

    return result


def query_skills(cursor: sqlite3.Cursor, sql: str) -> Any:
    result: dict[str, list[dict[str, str]]] = {}

    query = cursor.execute(sql).fetchall()
    for category, skill in query:
        if category not in result:
            result[category] = []

        result[category].append(skill)

    return result


def query_education(cursor: sqlite3.Cursor, sql: str) -> Any:
    result: dict[str, list[dict[str, str]]] = {}

    query = cursor.execute(sql).fetchall()
    for school, *concentration, date_awarded in query:
        if school not in result:
            result[school] = []

        concentration.append(date_awarded)
        result[school].append(concentration)

    return result


def main():
    with (
        sqlite3.connect(
            f"file:{os.environ.get('DATABASE')}?mode=ro",
            uri=True,
            detect_types=sqlite3.PARSE_COLNAMES,
        ) as con,
        SQLQueryHandler("query_experience.sql") as experience_query,
        SQLQueryHandler("query_projects.sql") as projects_query,
        SQLQueryHandler("query_skills.sql") as skills_query,
        SQLQueryHandler("query_education.sql") as education_query,
    ):
        con.row_factory = sqlite3.Row
        cursor = con.cursor()

        experience = query_experience(cursor, experience_query)
        projects = query_projects(cursor, projects_query)
        skills = query_skills(cursor, skills_query)
        education = query_education(cursor, education_query)

    return experience, projects, skills, education
