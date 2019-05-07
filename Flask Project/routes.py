from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world"

@app.route("/bye")
def bye():
    return "Bye"

if __name__ == "__main__":
    app.run()