from flask import Flask

app = Flask(__name__)

# Implemented by Tomer
@app.route("/")
def room():
    return "hi"


if __name__ == "__main__":
    app.run()