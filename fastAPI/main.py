from fastapi import FastAPI
from mockData import products
from fastapi import Request

app = FastAPI()

@app.get("/")
def home():
    return "Ilma is doomed!!"

@app.get("/contact")
def contact():
    return "Only akshat and priya can contact me....."

@app.get("/products")
def get_product():
    return products

##path param
@app.get("/product/{product_id}")
def get_one_product(product_id:int):
    
    for oneProduct in products:
        if oneProduct.get(id) == product_id:
            return oneProduct
    return {
        "error": "product not found for this ID."
    }

## query paam 
@app.get("/greet")
def greet_user(name:str, age:int):
    return {
        "greet":" hii {name} , your age is {age}"
    }

##to call api from any platfrom 
@app.get("/greet")
def greet_user(request:Request):
    return {
        "greet":" hii {name} , your age is {age}"
    }

