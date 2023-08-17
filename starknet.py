import datetime
import logging
import requests
from web3 import Web3
import time
from config import retries, RPC_STARK, max_gas

from starknet_py.net.account.account import Account
from starknet_py.net.full_node_client import FullNodeClient
from starknet_py.net.models.chains import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair

class StarkNet():
    def __init__(self, private_key, web3, number, max_gas, log) -> None:
        self.log = log
        self.private_key = private_key
        self.web3 = web3
        self.max_gas = max_gas
        self.number = number
        self.account = self.web3.eth.account.from_key(private_key)
        self.address_wallet = self.account.address

    def get_balance(self) -> float:
        """Get ETH balance of a given Ethereum address."""
        
        # Fetch balance in Wei
        balance_wei = self.web3.eth.get_balance(self.address_wallet)
        print(self.address_wallet)
        # Convert Wei to Ether and return
        balance_eth = self.web3.from_wei(balance_wei, ' ether')
        return balance_eth
     
    def check_gas_eth(self, max_gas):
            try:
                url_rpc = 'https://rpc.ankr.com/eth'
                eth_w3 = Web3(Web3.HTTPProvider(url_rpc, request_kwargs={'timeout': 60}))
                while True:
                    res_ = int(round(Web3.from_wei(eth_w3.eth.gas_price, 'gwei')))
                    self.log.info(f'Газ сейчас - {res_} gwei\n')
                    if res_ <= max_gas:
                        break
                    else:
                        time.sleep(100)
                        continue
            except:
                return 0
            
if __name__ == '__main__':
    with open("pk.txt", "r") as f:
        keys_list = [row.strip() for row in f]
        log = logging.getLogger()
        console_out = logging.StreamHandler()
        basic_format = logging.Formatter('%(asctime)s : %(message)s')
        file_handler = logging.FileHandler(f"LOGS/logs.txt", 'a', 'utf-8')
        file_handler.setFormatter(basic_format)
        log.setLevel(logging.DEBUG)
        log.addHandler(console_out)
        log.addHandler(file_handler)

    while keys_list:
        pk = keys_list.pop(0)
        # There is another way of creating key_pair
        key_pair = KeyPair.from_private_key(key=pk)

        client = FullNodeClient(node_url=RPC_STARK)
        account = Account(
            client=client,
            address=RPC_STARK,
            key_pair=key_pair,
            chain=StarknetChainId.TESTNET,
        )

        print(account.get_balance())