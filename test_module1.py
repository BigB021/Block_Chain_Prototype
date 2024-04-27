## Test data list
from block_chain import BlockChain


data_list = ["Block 1 Data", "Block 2 Data", "Block 3 Data", "Block 4 Data"]

# Initialize blockchain
blockchain = BlockChain()

# Add blocks to the blockchain using the data from the data list
for data in data_list:
    successful = blockchain.add_new_block(data)
    if not successful:
        print("Failed to add block due to blockchain validation failure.")
    blockchain.print_block_chain()

# Final integrity check
print("Final Blockchain Integrity Check:", "Valid" if blockchain.is_valid() else "Invalid")
