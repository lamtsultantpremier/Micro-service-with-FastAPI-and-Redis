from schema import Product
from fastapi import status, HTTPException

def format(pk : str):
    product = Product.get(pk)

    return{
        'id':product.pk,
        'name':product.name,
        'price' : product.price,
        'quantity' : product.quantity
    }

def create_product(product : Product):
    product_saved = Product.save(product)
    return product_saved

def get_all_products():
    products = [format(pk) for pk in Product.all_pks()]
    
    if products is None:
        raise HTTPException(detail = "Product not exist in database", status_code = status.HTTP_404_NOT_FOUND)
    
    return products

def get_product(pk : str):
    if pk not in Product.all_pks():
        raise HTTPException(detail = "product with this id not found",status_code = status.HTTP_404_NOT_FOUND)
    
    return Product.get(pk)

def delete_product(pk : str):
    Product.delete(pk)
    return f"Product successfully delete"

def product_update(pk : str, product : Product):
    product_sended = Product.get(pk)
    if product_sended is None:
        raise HTTPException(detail = "Product with this id not found" , status_code = status.HTTP_404_NOT_FOUND)
    
    product_sended.name = product.name if product.name is not None else product_sended.name
    product_sended.price = product.price if product.price is not None else product_sended.price
    product_sended.quantity = product.quantity if product.quantity is not None else product_sended.quantity
    Product.save(product_sended)
    return product_sended
