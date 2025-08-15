from database_config import redis_connection
from schema import Order
import time

key = 'refund_order'
group = 'payment-group'

try:
    redis_connection.xgroup_create(key , group)
except:
   print("Group already exist")

while True:
    try:
       results = redis_connection.xreadgroup(group , key , {key : '>'} , None)

       if results != []:
           for result in results:
               obj = result[1][0][1]
               order = Order.get(obj["pk"])
               order.status = "refunded"
               order.save()
               print(order)

    except Exception as e:
        print(str(e))
        
    time.sleep(1)