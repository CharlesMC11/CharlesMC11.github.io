#!/usr/bin/env python

from pathlib import Path

from flask_frozen import Freezer

from app import app

if __name__ == "__main__":
    freezer = Freezer(app)
    freezer.freeze()

    for file in Path(__file__).with_name("app").joinpath("build").iterdir():
        if file.is_file() and not file.suffix:
            new_name = file.with_suffix(".html")

            file.rename(new_name)
