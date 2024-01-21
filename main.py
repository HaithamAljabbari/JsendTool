from web3 import Web3
import pyfiglet
import sys
from termcolor import cprint

# create an instance of `Web3` connected to the geth server
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/77ade6c8526e46d0accb0a6def8012ca'))      # `geth` creates the server at `http://127.0.0.8545`


print(pyfiglet.figlet_format("JSEND TOOL", font="digital"))


file = sys.argv[1]
price = int(sys.argv[2])    

with open(file, "r") as f:
	wallets = f.read()

wallet_list = wallets.split()

sender = wallet_list[0]
receiver = wallet_list[1]

cprint("Transaction started", "green")
# create and sign a transaction

try:
	tx_hash = w3.eth.send_transaction({        # `w3.eth.send_transaction` returns a transaction hash
    	'to': receiver,
    	'from': sender,
    	'value': w3.to_wei(price, 'ether'),    # convert the amount of ethers to Wei
	})
	receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
	cprint(receipt, "orange")
	cprint("Transaction successful", "green")
except ValueError:
	cprint("Error: Insufficient funds for gas", "red")

# Wait for Geth to mine the transaction

# Confirm that the Ethers were sent
print("sender's account: ", w3.eth.get_balance(sender))
print("receiver's account: ", w3.eth.get_balance(receiver))