import os
from flask import send_from_directory
from flask import Flask, render_template, request, redirect, url_for, session
from game import new_game, move_player, items_at_location, collect_item, restore_beacon

app = Flask(__name__)
app.secret_key = os.environ.get(
    "SECRET_KEY",
    "local-development-only-secret"
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/start", methods=["GET", "POST"])
def start_game():
    if request.method == "POST":
        name = request.form.get("name", "").strip()

        if not name:
            name = "Explorer"

        session["player"] = new_game(name)
        return redirect(url_for("play"))

    return render_template("start.html")


@app.route("/play")
def play():
    player = session.get("player")

    if not player:
        return redirect(url_for("start_game"))

    available_items = items_at_location(player)

    return render_template(
        "game.html",
        player=player,
        available_items=available_items
    )


@app.route("/move", methods=["POST"])
def move():
    player = session.get("player")

    if player:
        destination = request.form.get("destination", "")
        move_player(player, destination)
        session["player"] = player

    return redirect(url_for("play"))


@app.route("/collect", methods=["POST"])
def collect():
    player = session.get("player")

    if player:
        available = items_at_location(player)

        if available:
            collect_item(player, available[0])

        session["player"] = player

    return redirect(url_for("play"))


@app.route("/restore", methods=["POST"])
def restore():
    player = session.get("player")

    if player:
        restore_beacon(player)
        session["player"] = player

    return redirect(url_for("play"))

@app.route("/sw.js")
def service_worker():
    response = send_from_directory("static/js", "sw.js")
    response.headers["Service-Worker-Allowed"] = "/"
    response.headers["Cache-Control"] = "no-cache"
    return response

if __name__ == "__main__":
    app.run(debug=True)
