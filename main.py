
from fastapi import FastAPI, HTTPException, Body
from middleware import log_requests_middleware

from models import Order

app = FastAPI()

app.middleware("http")(log_requests_middleware)

@app.post("/create_order/", response_model = Order)
def send_order(order: Order):
    
    print(order)
    return order
