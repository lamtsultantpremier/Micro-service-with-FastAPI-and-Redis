from redis_om import HashModel
from database_config import redis_connection
from dataclasses import dataclass

class Order(HashModel):
    product_id: str
    price : float
    fee : float
    total : float
    quantity : int
    status : str

    class Meta:
        database = redis_connection

class Product:
    pk:str
    name : str
    price : float
    quantity : int