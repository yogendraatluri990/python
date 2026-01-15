from fastapi import FastAPI, HTTPException

from constants.block_chain_enum import BlockChainEnum

from app.block_chain import validate_block_chain_option

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to FAST API"}

 
@app.get("/items/{item_id}")
async def get_items_by_id(item_id: str):
     i_id = item_id.strip()   
     if len(i_id) <=0 or i_id == '':
          raise HTTPException(status_code=400, detail="Invalid Item Id")
     return {"item_id": item_id}

@app.get("/blockchain_type")
@validate_block_chain_option
async def get_blockchain_by_name(blockChainName: BlockChainEnum):
     # The decorator handles the logic and returns the message
     # This code won't execute because the decorator returns directly
     return {"message": f"Fallback for {blockChainName.value}"}
     
          