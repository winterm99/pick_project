# Imports

from flask import Flask, render_template, request, redirect
import random
import string
# notwendig um in render variablen zu lesen !!
import os

app = Flask(__name__)

polls = {}


# Routen

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


# Code erstellen

def generate_code(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


# Umfrage erstellen

@app.route("/create", methods=["POST"])
def create():

    # aus html daten holen
    question = request.form.get("question")
    answers = request.form.getlist("answer")

    # keine leeren Umfragen
    if not question or not answers:
        return "Invalid input"

    code = generate_code()

    # Daten speichern 
    polls[code] = {
        "question": question,
        "answers": answers,
        "votes": [0] * len(answers)
    }

    # Fügt code in Url ein  und leitet weiter
    return redirect(f"/poll/{code}")


# Umfrage anzeigen (<code> ist in der url)

@app.route("/poll/<code>")
def poll(code):
                       
    poll = polls.get(code)

    if not poll:
        return "Poll not found"

    # html anzeigen
    return render_template("poll.html", poll=poll, code=code)


@app.route("/join", methods=["POST"])
def join():

    # code holen in großbuchstaben
    code = request.form.get("code", "").upper()

    # prüfen
    if not code:
        return "Please enter a code"

    if code not in polls:
        return "Invalid code"

    # weiterleiten zu choose seite
    return redirect(f"/choose/{code}")


# Seite zum abstimmen

@app.route("/choose/<code>")
def choose(code):
    poll = polls.get(code)

    if not poll:
        return "Poll not found"

    return render_template("choose.html", poll=poll, code=code)


# Stimme abgeben 

@app.route("/vote/<code>", methods=["POST"])
def vote(code):
    poll = polls.get(code)

    if not poll:
        return "Poll not found"

    # Auswahl holen von html
    choice = request.form.get("vote")

    # Prüfen
    if choice is None:
        return "No option selected"

    # Stimme zählen
    choice = int(choice)
    poll["votes"][choice] += 1

    # zurück zur umfrage übersicht
    return redirect(f"/poll/{code}")


# Server nur starten, wenn app.py direkt ausgeführt wird

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)