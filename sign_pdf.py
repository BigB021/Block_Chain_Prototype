# Example usage of the Wallet class to sign a pdf document and verify the digital signature
from block_chain import BlockChain, Wallet


blockchain = BlockChain()
wallet = Wallet()
public_key = wallet.get_public_key()

signature = wallet.sign_document('pdfs/BlockchainPaper.pdf')
if signature:
    is_verified = wallet.verify_signature('pdfs/BlockchainPaper.pdf', signature)
    print(f"Verification result: {is_verified}")
else:
    print("Document signing failed.")
blockchain.print_block_chain()