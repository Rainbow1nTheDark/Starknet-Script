from web3 import Web3
from starknet import StarkNet

class Avnu(StarkNet):
    def __init__(self, private_key, web3, number, max_gas, log) -> None:
        self.log = log
        self.private_key = private_key
        self.web3 = web3
        self.max_gas = max_gas
        self.number = number
        self.account = self.web3.eth.account.from_key(private_key)
        self.address_wallet = self.account.address
        self.address = Web3.to_checksum_address('0xc662c410C0ECf747543f5bA90660f6ABeBD9C8c4')
        # self.abi = js.load(open('./abi/main_bridge.txt'))
        # self.contract = self.web3.eth.contract(address=self.address, abi=self.abi)

    def get_balance(eth_address: str) -> float:
        """Get ETH balance of a given Ethereum address."""
        
        # Fetch balance in Wei
        balance_wei = w3.eth.getBalance(eth_address)
        
        # Convert Wei to Ether and return
        balance_eth = w3.fromWei(balance_wei, 'ether')
        return balance_eth