from flask import Flask, render_template

import query

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return render_template("index.html")


@app.route("/3d")
def three_d() -> str:
    return render_template("3d.html")


@app.route("/photo")
def photography() -> str:
    return render_template("photography.html")


@app.route("/cv")
def cv() -> str:
    experience, projects, skills, education = query.main()

    return render_template(
        "cv/base.html",
        experience=experience,
        projects=projects,
        skills=skills,
        education=education,
    )


@app.route("/about-me")
def about_me():
    return render_template("about-me.html")
