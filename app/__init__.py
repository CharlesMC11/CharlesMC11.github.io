import os

from dotenv import load_dotenv
from flask import Flask, render_template

from .cv import bp as cv_bp

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

app.register_blueprint(cv_bp)


@app.get("/")
def index() -> str:
    return render_template("index.html")


@app.get("/about")
def about_me() -> str:
    return render_template("about-me.html")
