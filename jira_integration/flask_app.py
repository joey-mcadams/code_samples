import base64

from flask import Flask
import elastic_info_getter
from matplotlib.figure import Figure
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def show_graph():
    data = elastic_info_getter.ElasticInfoGetter().get_array_of_hits_per_minute()


    # Generate the figure **without using pyplot**.
    fig = Figure()
    ax = fig.subplots()
    ax.plot(data)

    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return f"<b>Critical Tickets per Minute Over the Last Hour:</b><br><img src='data:image/png;base64,{data}'/>"


