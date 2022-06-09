from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def return_home():

    return render_template("select_menu.html")

@app.get("/questions")
def return_home():

    story = request.args["stories"]
    return render_template("questions.html", story = silly_story.prompts)


@app.get("/results")
def render_story():

    word_list = {}

    for word in silly_story.prompts:
        value = request.args[word]
        word_list[word] = value

    rendered_story = silly_story.generate(word_list)

    return render_template("story.html", html_story = rendered_story)
