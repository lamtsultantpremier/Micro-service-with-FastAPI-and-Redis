from schema import Order,Product
from fastapi  import HTTPException,status
import time
from database_config import redis_connection
def create_order(product : Product):
        order = Order(
                product_id = product.pk,
                price = product.price,
                fee = product.price * 0.2,
                total = product.price * 1.2)

def order_completed(order : Order):
    time.sleep(5)
    order.status = "completed"
    order.save()
    redis_connection.xadd('order_completed',order.model_dump(),'*')

def get_orders():
    orders = [format_order(pk) for pk in Order.all_pks()]
    if orders is None:
         raise HTTPException(detail = "No product found",status_code = status.HTTP_404_NOT_FOUND)
    
    return orders

def format_order(pk : str):
    return Order.get(pk)
