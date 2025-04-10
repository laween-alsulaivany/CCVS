from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return "<h1>Hello! Welcome to CSIS Chess!</h1><h3>Put /'your_name' at the end of the url to see something cool!</h3>"

@app.route("/<name>")
def user(name):
    dons = ["Donovan", "Donnie", "Donny"]
    if name in dons:
        return f"{name} is awesome!"
    else:
        return f"{name} is a bitch!"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=80)