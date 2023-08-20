
from fastapi import FastAPI, HTTPException, Body

from models import Order

app = FastAPI()

@app.post("/create_order/", response_model = Order)
def send_order(order: Order = Body(...)):
    
    print(order)

    with open("last_order.txt", "w") as file:
        file.write(str(order))

    return order
