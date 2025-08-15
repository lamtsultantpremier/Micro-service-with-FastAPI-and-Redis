from fastapi import FastAPI,HTTPException,status
from schema import Product
from fastapi.middleware.cors import CORSMiddleware
from services import format
import services
import configs

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = [configs.FRONT_URL],
    allow_methods = ['*'],
    allow_headers = ['*']
)

@app.get("/")
async def root():
    return {"message":"welcome"}

@app.get("/products")
def all_products():
    return [format(pk) for pk in Product.all_pks()]

@app.post("/products")
def create_products(product : Product):
    product_saved = services.create_product(product)
    return product_saved

@app.get("/products/{pk}")
def get_product(pk : str):
    product = services.get_product(pk)
    return product

@app.delete("/products/{pk}")
def delete_product(pk : str):
    pk = services.delete_product(pk)
    return pk
@app.put("/products/{pk}")
def update_product(pk:str , product:Product):
    product_updated = services.product_update(pk , product)
    return product_updated