
from pydantic import BaseModel

class Order(BaseModel):
    order_id: int
    state: str
    total: float
    phone: str
