
from uuid import UUID
from pydantic import BaseModel


class BlockData(BaseModel):
    sender: str
    receiver: str
    amount: float

class BlockChain(BaseModel):
    index: UUID
    data: BlockData
    previous_index: UUID | None