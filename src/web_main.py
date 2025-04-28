#This file is the website
from flask import Flask, render_template, url_for, redirect, request
import chess
import board_display

board = chess.Board()

def get_ip():
    # Try to get real IP if behind a proxy/load balancer
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # X-Forwarded-For may contain multiple IPs (client, proxy, etc.)
    if ip and ',' in ip:
        ip = ip.split(',')[0].strip()

    # Do something with the IP (e.g., log it)
    print(f"Visitor IP: {ip}")
    return f"Your IP address is: {ip}"


app = Flask(__name__)
# This is the starting page
@app.route("/", methods=["POST", "GET"])

def index():
    # When the button is pressed it sends a post command, redericting it to the chess page
    if request.method == "POST":
        return redirect(url_for("chess"))
    else:
        return render_template("index.html" )

# This is the chess page
@app.route("/chess", methods=["POST", "GET"])
# Message displays if the vote was successful, move is the vote the user submitted, output is the board, and color is the team.
def chess():
    message = ""
    # If a vote is made it will change move to that vote and change message.
    if request.method == "POST":
        move = request.form.get("move", "")
        message = board_display.legal_move(board, move)
        
        if message == "Your vote was successful":
            ip = request.headers.get('X-Forwarded-For', request.remote_addr)
            if ip and ',' in ip:
                ip = ip.split(',')[0].strip()
            with open("static/votes.txt", "a") as f:
                f.write(f"{move} - {ip}\n")

    return render_template("chess.html",
        output=board_display.displayBoardAsString(board).replace("\n", "<br>"),
        color=board_display.team(board),
        message=message
    )

# This is the url the website runs on
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)