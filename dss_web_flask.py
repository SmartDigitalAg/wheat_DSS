import io
import redis
from flask import Flask, request, render_template, Response
import time

app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

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
        cache_key = f"{graph_type}:{date_today_month}:{date_today_day}"

        cached_image = r.get(cache_key)
        if cached_image:
            return Response(cached_image, content_type="image/png")

        with open(img_path, "rb") as image_file:
            image_data = image_file.read()
            r.set(cache_key, image_data)

        time.sleep(10)
        return Response(image_data, content_type="image/png")

    return "Invalid graph type or date"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
