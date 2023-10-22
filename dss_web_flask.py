import io
from flask import Flask, request, render_template, Response
import time

app = Flask(__name)

def generate_graph(graph_type, date_today_month, date_today_day):
    date_today_month = str(date_today_month).zfill(2)
    date_today_day = str(date_today_day).zfill(2)

    if graph_type == 'yield_graph':
        img_path = f'pawees/yield/yield_{date_today_month}{date_today_day}.png'
    elif graph_type == 'sws_graph':
        img_path = f'pawees/swc/swc_{date_today_month}{date_today_day}.png'
    elif graph_type == 'rain_graph':
        img_path = f'pawees/rain/rain_{date_today_month}{date_today_day}.png'
    else:
        img_path = None

    return img_path

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<graph_type>/<int:date_today_month>/<int:date_today_day>")
def main(graph_type, date_today_month, date_today_day):
    img_path = generate_graph(graph_type, date_today_month, date_today_day)

    if img_path:
        with open(img_path, "rb") as image_file:
            image_data = image_file.read()

        time.sleep(10)
        return Response(image_data, content_type="image/png")

    return "Invalid graph type or date"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
