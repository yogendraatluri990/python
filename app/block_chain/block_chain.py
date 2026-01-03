from functools import wraps
import uuid


from schemas import BlockChain



block_chain:list[BlockChain] = []

# @DECORATORS
def construct_block_chain(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
      print(f"Args are {args}, Kwargs are {kwargs}")
      if len(args) > 0:
         b_chain = BlockChain(
            index=uuid.uuid4(),
            data={
                "sender": f"Alice-{args[0]}",
                "receiver": f"Bob-{args[0]}",
                "amount": 50.0 + float(args[0])
            },
            previous_index=None
         )
         return func(b_chain, **kwargs)  # Pass kwargs too!
      return func(*args, **kwargs)
    return wrapper

def read_user_input(func: callable):
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
    

    

for n in range(5):
    print(f"n is {n} is_last iteration: {n == 4}")
    generate_block_chains(n+1, is_last= (n==4))


def validate_block_chain(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        block_chain = args[0]
        if type(block_chain) is BlockChain and kwargs.get('previous_index') == block_chain.previous_index:
             is_block_valid = True
             return func(is_block_valid)
        
    return wrapper

@validate_block_chain
def assert_block_chain(is_block_chain_valid: bool):
      print(f"Is Block Chain Valid: {is_block_chain_valid}")


for block in block_chain:
    assert_block_chain(block, previous_index=block.previous_index) # The second argument is for decorator validation.
     
