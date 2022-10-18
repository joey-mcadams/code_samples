from flask import Flask

app = Flask(__name__)

@app.route("/")
def show_graph():
    return "<p>Data will happen here!</p>"