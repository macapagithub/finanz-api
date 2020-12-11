from pydantic import BaseModel
from datetime import datetime

class TransactionIn(BaseModel):
    username: str 

class TransactionOut(BaseModel):
    id_transaction: int
    username: str
    date: datetime

