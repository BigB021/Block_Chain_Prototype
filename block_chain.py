import hashlib
import ecdsa
import base64
from PyPDF2 import PdfReader

class Block:
    """
    A Block class represents each block in the blockchain.
    """
    def __init__(self, previous_hash, data):
        self.previous_hash = previous_hash
        self.data = data
        self.data_string = f"{previous_hash}{data}"
        self.hash = self.calculate_hash(self.data_string)
    
    @staticmethod
    def calculate_hash(data_string):
        """
        Calculate SHA256 hash of the data string.
        """
        return hashlib.sha256(data_string.encode()).hexdigest()

class BlockChain:
    """
    A BlockChain class manages the chain of blocks.
    """
    def __init__(self):
        self.blocks = [self.create_genesis_block()]
        
    def create_genesis_block(self):
        """
        Creates the initial (genesis) block of the blockchain.
        """
        print("Creating the Genesis block...")
        return Block("0" * 64, "Genesis Block")
    
    def is_valid(self):
        """
        Check the integrity of the blockchain.
        """
        print("Checking blockchain integrity...")
        for i in range(1, len(self.blocks)):
            current = self.blocks[i]
            previous = self.blocks[i - 1]
            if current.hash != Block.calculate_hash(current.data_string):
                print("Block integrity error found!")
                return False
            if current.previous_hash != previous.hash:
                print("Chain linkage error!")
                return False
        return True
         
    def add_new_block(self, data):
        """
        Add a new block to the blockchain after validation.
        """
        print(f"Adding new block with data: {data}")
        last_block = self.blocks[-1]
        new_block = Block(last_block.hash, data)
        if self.is_valid():
            self.blocks.append(new_block)
            print("New block added successfully.")
            return True
        else:
            print("Failed to add new block. Blockchain is invalid.")
            return False
        
    def print_block_chain(self):
        """
        Print all blocks in the blockchain.
        """
        for block in self.blocks:
            print(f"{block.data_string} -> ", end="")
        print("\n")

class Wallet:
    """
    A Wallet can generate keys, sign documents, and verify signatures.
    """
    def __init__(self):
        self.signing_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.verifying_key = self.signing_key.get_verifying_key()
    
    def get_public_key(self):
        """
        Return the hex representation of the public key.
        """
        return self.verifying_key.to_string().hex()
    
    def sign_document(self, document_path):
        """
        Sign the document using ECDSA and return the signature.
        """
        print(f"Signing document: {document_path}")
        try:
            with open(document_path, 'rb') as file:
                reader = PdfReader(file)
                content = "".join([page.extract_text() for page in reader.pages if page.extract_text()])
                document_hash = hashlib.sha256(content.encode()).digest()
            signature = self.signing_key.sign(document_hash)
            print("Document signed successfully.")
            return base64.b64encode(signature).decode()
        except Exception as e:
            print(f"Error signing document: {e}")
            return None
    
    def verify_signature(self, document_path, signature):
        """
        Verify the signature of the document.
        """
        print(f"Verifying signature for document: {document_path}")
        try:
            with open(document_path, 'rb') as file:
                reader = PdfReader(file)
                content = "".join([page.extract_text() for page in reader.pages if page.extract_text()])
                document_hash = hashlib.sha256(content.encode()).digest()
            signature = base64.b64decode(signature)
            verification = self.verifying_key.verify(signature, document_hash)
            print("Signature verified successfully." if verification else "Signature verification failed.")
            return verification
        except Exception as e:
            print(f"Error verifying signature: {e}")
            return False

