from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.background import BackgroundTasks

from starlette.requests import Request
import services
import configs
from schema import Order
import requests

from database_config import redis_connection

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = [configs.dotenv_values],
    allow_methods = ['*'],
    allow_headers = ['*']
)

@app.get("/")
def index():
    return redis_connection.info()

@app.post("/orders")
async def create_order(request : Request , background_task : BackgroundTasks):
   body = await request.json()
   product = requests.get(url = f'http://localhost:8000/products/{body["id"]}').json()

   order = Order(
       product_id = product["pk"],
       price = product["price"],
       fee = product["price"] * 0.2,
       total = product["price"] * 1.2,
       quantity = body["quantity"],
       status = "pending"
   )
   order.save()
   background_task.add_task(services.order_completed,order)
   return order

@app.get("/orders")
def get_all_orders():
    orders = services.get_orders()
    return orders

@app.get("/orders/{pk}")
def get_order(pk : str):
    order = Order.get(pk)
    redis_connection.xadd('refund_order', order.model_dump() , '*')
    return order

