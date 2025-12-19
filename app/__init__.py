import os

from flask import Flask, render_template

from .auth import bp as auth_bp
from .cv import bp as cv_bp
from .photography import bp as photo_bp
from .three_d import bp as three_d_bp

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

app.register_blueprint(auth_bp)
app.register_blueprint(cv_bp)
app.register_blueprint(photo_bp)
app.register_blueprint(three_d_bp)


@app.get("/")
def index() -> str:
    return render_template("index.html")


@app.get("/about")
def about_me() -> str:
    return render_template("about-me.html")
