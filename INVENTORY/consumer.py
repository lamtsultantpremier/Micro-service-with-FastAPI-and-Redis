from database import redis_connection
from schema import Product
import time

key = 'order_completed'
group = 'inventory-group'

try:
    redis_connection.xgroup_create(key , group)
except:
   print("Group already exist")

while True:
    try:
       results = redis_connection.xreadgroup(group , key , {key : '>'} , None)
       print(results)
       if results != []:
           for result in results:
                obj = result[1][0][1]

                try:
                    product = Product.get(obj["product_id"])
                    print(product)
                    product.quantity = product.quantity - int(obj["quantity"])
                    product.save()
                except:
                   redis_connection.xadd('refund_order', obj , '*')
                
    except Exception as e:
        print(str(e))

    time.sleep(1)