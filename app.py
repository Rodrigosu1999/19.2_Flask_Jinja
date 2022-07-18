from stories import story
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
debug = DebugToolbarExtension(app)


@app.route("/")
def index():
    """ Home: here will be the form to enter the propmts"""

    prompts = story.prompts
    return render_template("home.html", prompts=prompts)


@app.route("/story")
def display_story():
    """After submitting the form, the full story will be displayed as text"""
    story_text = story.generate(request.args)
    return render_template("story.html", story_text=story_text)
