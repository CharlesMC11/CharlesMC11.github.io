from datetime import date

from jinja2 import UndefinedError

from build import _date_formatter


def test__date_formatter():

    x = date(2011, 1, 9)
    assert _date_formatter(x) == "Jan\u00a02011"
    assert _date_formatter(None) == "Present"
    assert _date_formatter(UndefinedError) == "Present"
