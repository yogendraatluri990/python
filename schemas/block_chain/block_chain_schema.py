
from uuid import UUID
from pydantic import BaseModel

from typing import TypedDict


class CountryDist(TypedDict):
    country_name: str
    country_code: str

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str
    country: CountryDist


class BlockUser(BaseModel):
    user_id: UUID
    first_name: str
    last_name: str
    address:Address | None





class BlockChain(BaseModel):
    index: UUID
    hash_index: str
    transactions: list[BlockTransaction]
    previous_index: UUID | None



class BlockTransaction(BaseModel):
     transaction_id: UUID
     recepient: BlockUser
     sender: BlockUser
     amount: float
     timestamp: str


