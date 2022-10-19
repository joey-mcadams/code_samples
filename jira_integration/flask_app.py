from flask import Flask

app = Flask(__name__)

@app.route("/")
def show_graph():
    return "<p>Data will happen here!</p>"

def get_all_records_in_the_last_hour():
    pass