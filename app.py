from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story
from stories import excited_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.get("/")
def return_home():
    """"""
    return render_template("select_menu.html")

@app.get("/questions")
def return_questions():
    """"""
    if request.args["stories"] == "silly_story":
        story = silly_story
    else:
        story = excited_story
    return render_template("questions.html", story = story.prompts, story_title=story)


@app.get("/results")
def render_story():
    """"""
    word_list = {}
    story = story_title

    for word in story.prompts:
        value = request.args[word]
        word_list[word] = value

    rendered_story = story.generate(word_list)

    return render_template("story.html", html_story = rendered_story)
