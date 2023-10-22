from web3 import Web3
from web3.middleware import geth_poa_middleware

API_URL = "https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3"
web3 = Web3(Web3.HTTPProvider(API_URL))

block_data = web3.eth.get_block('latest')
print('latest block of etherum : ', block_data)

block_transaction_count = web3.eth.get_block_transaction_count(13042315)
print('Number of transactions happened in the block ', block_transaction_count)

Transaction_fee= web3.eth.fee_history(block_count=512, newest_block="latest", reward_percentiles=None)
print("Number of Transactions happened in the block: ", Transaction_fee)


