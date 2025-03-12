from flask import Flask, render_template

app = Flask(__name__)

# Implemented by Tomer
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/GET /<room>", methods= ['GET'])
def room(room):
    return render_template("index.html")

if __name__ == "__main__":
    app.run()