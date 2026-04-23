from flask import Flask, render_template, request, redirect
import random
import string

app = Flask(__name__)

polls = {}

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create")
def create_page():
    return render_template("create.html")


@app.route("/joinpoll")
def joinpoll():
    return render_template("joinpoll.html")


@app.route("/help")
def help():
    return render_template("help.html")


def generate_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


@app.route("/create", methods=["POST"])
def create():
    question = request.form.get("frage")
    answers = request.form.getlist("answer")

    if not question or not answers:
        return "Invalid input"

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


@app.route("/join", methods=["POST"])
def join():
    code = request.form.get("code", "").upper()

    if not code:
        return "Please enter a code"

    if code not in polls:
        return "Invalid code"

    return redirect(f"/choose/{code}")


@app.route("/choose/<code>")
def choose(code):
    poll = polls.get(code)

    if not poll:
        return "Poll not found"

    return render_template("choose.html", poll=poll, code=code)


if __name__ == "__main__":
    app.run(debug=True)