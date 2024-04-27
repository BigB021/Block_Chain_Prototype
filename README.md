# Block_Chain_Prototype
This project demonstrates the implementation of blockchain technology and digital signing of PDF documents using Python. The project is divided into one classes module and three main modules:

    block_chain.py: Implementation of Block,Block_Chain and Wallet classes
    bitcoin.py: Processes and blockchains data from a CSV file.
    sign_pdf.py: Digitally signs and verifies the signatures of PDF documents.
    test_module1.py: Tests the functionality of the blockchain implementation using a series of predefined data blocks.

## Installation

Before running the project, ensure you have Python installed on your system. The project requires Python 3.6 or newer. You will also need to install several dependencies:
Prerequisites

    Python 3.6+
    Pip (Python package installer)

## Dependencies

Install the required Python packages using pip:


pip install PyPDF2 ecdsa hashlib base64

## Modules Description
1- **bitcoin.py**

This script reads a CSV file containing data and processes it into a blockchain. Each row in the CSV becomes a block in the chain. The script is designed to demonstrate how data from traditional formats can be used within a blockchain context.
### Usage:

python bitcoin.py

2- **sign_pdf.py**

Allows the signing and verification of PDF documents using ECDSA (Elliptic Curve Digital Signature Algorithm). This module demonstrates the application of blockchain-related security measures in document handling.
### Usage:


To sign a PDF document
python sign_pdf.py sign <path_to_pdf>

To verify a signed PDF document
python sign_pdf.py verify <path_to_pdf> <signature>

3- **test_module1.py**

A testing script that validates the functionality of the blockchain implementation. It adds a series of data blocks to a blockchain and verifies the integrity of the chain throughout the process.
### Usage:

python test_module1.py


## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your changes or improvements.
License

This project is open source and available under the [MIT License](https://opensource.org/license/mit).

This README provides a comprehensive guide on what the project is about, how to set it up, and how to use each component. Adjust paths and commands based on your actual file structure and environment settings.

## 