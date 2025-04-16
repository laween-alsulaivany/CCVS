from flask import Flask, render_template, url_for, redirect, request
import chess
import board_display

board = chess.Board()


app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        return redirect(url_for("chess"))
    else:
        return render_template("index.html" )

@app.route("/chess", methods=["POST", "GET"])
def chess():
    message = ""
    if request.method == "POST":
        move = request.form.get("move", "")
        message = board_display.legal_move(board, move)

    return render_template("chess.html",
        output=board_display.displayBoardAsString(board).replace("\n", "<br>"),
        color=board_display.team(board),
        message=message
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80)