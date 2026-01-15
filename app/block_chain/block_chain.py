from functools import wraps
import inspect
from unittest import case
import uuid
from typing import Callable, Any, Awaitable

from constants.block_chain_enum import BlockChainEnum
from schemas import Address, BlockChain, BlockUser, BlockTransaction



block_chain:list[BlockChain] = []

def generate_user_data(block_index: int) -> BlockUser:
    return BlockUser(
       user_id = uuid.uuid4(),
       first_name= f"John_{block_index}",
       last_name= f"Doe_{block_index}",
       address=Address(
          street= f"1234 Elm St_{block_index}",
          city= f"Springfield_{block_index}",
          state= f"IL_{block_index}",
          zip_code= f"62704_{block_index}",
          country= {"country_name": "United States", "country_code": "US"}
    )
    )

# @DECORATORS
def construct_block_chain(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
      print(f"Args are {args}, Kwargs are {kwargs}")
      if len(args) > 0:
         transaction_list = BlockTransaction(
            transaction_id=uuid.uuid4(),
            recepient= generate_user_data(args[0]),
            sender= generate_user_data(args[0]),
            amount = 1000.0 * float(args[0]),
            timestamp= "2024-10-01T12:00:00Z"
         )
         b_chain = BlockChain(
             index = uuid.uuid4(),
             hash_index= f"hash_{args[0]}",
             transactions= [transaction_list],
             previous_index= None
         )
         return func(b_chain, **kwargs)  # Pass kwargs too!
      return func(*args, **kwargs)
    return wrapper

def read_user_input(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        user_input = input("Enter Your Choice to Add Block Chain")
        return func(user_input, **kwargs)
    return wrapper


def save_block_chain(block_chain_list: list[BlockChain]):
    if len(block_chain_list) <=0:
        return None
    
    with open("block_chain_db.txt", "w") as f:
         for block in block_chain_list:
             f.write(f"{block.model_dump_json()} \n")

@read_user_input
@construct_block_chain
def generate_block_chains(new_block_chain: BlockChain, is_last = False):
    if len(block_chain) <= 0:
        block_chain.append(new_block_chain)
    else:
      block_chain.append(new_block_chain.model_copy(update={"previous_index": block_chain[-1].index}))

    if is_last:
        save_block_chain(block_chain)
    

    

# for n in range(5):
#     print(f"n is {n} is_last iteration: {n == 4}")
#     generate_block_chains(n+1, is_last= (n==4))


def validate_block_chain(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        block_chain = args[0]
        if type(block_chain) is BlockChain and kwargs.get('previous_index') == block_chain.previous_index:
             is_block_valid = True
        else :
                is_block_valid = False
        return func(is_block_valid)
        
    return wrapper

@validate_block_chain
def assert_block_chain(is_block_chain_valid: bool):
      print(f"Is Block Chain Valid: {is_block_chain_valid}")


# for block in block_chain:
#     assert_block_chain(block, previous_index=block.previous_index) # The second argument is for decorator validation.
     

# even_number = [n for n in range(100) if n%2 ==0]
# print(f" {even_number} ")


#Decorators
def validate_block_chain_option(func: Callable):
     @wraps(func)  
     async def wrapper(*args, **kwargs) -> dict[str, str]:
          blockChainName = kwargs.get("blockChainName")    
          match blockChainName:
            case BlockChainEnum.BITCOIN.value:
               return {"message": f"Blockchain selected is : {blockChainName}"}
            case BlockChainEnum.ETHEREUM.value:
               b_ethereum = BlockChainEnum.ETHEREUM               
               return  {"message": b_ethereum}
            case BlockChainEnum.RIPPLE.value:
               return {"message": f"Blockchain selected is :{blockChainName}"}
            case BlockChainEnum.LITECOIN.value:
               return  {"message": f"Blockchain selected is :{blockChainName}"}
            case _:
               return {"message": "Invalid block chain option"}         
     return wrapper