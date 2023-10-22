import asyncio
import io
import redis
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, db=0)

templates = Jinja2Templates(directory="templates")

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

@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/{graph_type}/{date_today_month:int}/{date_today_day:int}")
async def main(graph_type: str, date_today_month: int, date_today_day: int):
    img_path = generate_graph(graph_type, date_today_month, date_today_day)

    if img_path:
        cache_key = f"{graph_type}:{date_today_month}:{date_today_day}"

        cached_image = r.get(cache_key)
        if cached_image:
            return StreamingResponse(io.BytesIO(cached_image), media_type="image/png")

        with open(img_path, "rb") as image_file:
            image_data = image_file.read()
            r.set(cache_key, image_data)

        await asyncio.sleep(5)
        return StreamingResponse(io.BytesIO(image_data), media_type="image/png")

    return "Invalid graph type or date"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
