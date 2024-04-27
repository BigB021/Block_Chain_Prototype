# A test module of the Block_Chain class on a bitcoin dataset

import csv
from block_chain import BlockChain

# Function to load data from CSV and add it to the blockchain
def load_data_from_csv(filename, blockchain):
    with open(filename, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Create a string representation of the row, excluding 'No' column
            data = f"{row['date']},{row['exchange_rate']}"
            blockchain.add_new_block(data)

# Initialize the blockchain
blockchain = BlockChain([])

# Load data from CSV and add to blockchain
load_data_from_csv('datasets/bitcoin.csv', blockchain)

# Print the blockchain
blockchain.print_block_chain()    
    
