import random
import string
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

polls = {}

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create", methods=["POST"])
def create():
    question = request.form.get("frage")
    answers = request.form.getlist("answer")

    code = generate_code()

    polls[code] = {
        "question": question,
        "answers": answers,
        "votes": [0] * len(answers)
    }

    return redirect(f"/poll/{code}")

@app.route("/poll/<code>")
def poll(code):
    poll = polls.get(code)

    if not poll:
        return "Poll not found"

    return render_template("poll.html", poll=poll, code=code)


@app.route("/vote/<code>", methods=["POST"])
def vote(code):
    poll = polls.get(code)

    if not poll:
        return "Poll not found"

    choice = int(request.form.get("vote"))
    poll["votes"][choice] += 1

    return redirect(f"/poll/{code}")



if __name__ == "__main__":
    app.run(debug=True)


bla bla