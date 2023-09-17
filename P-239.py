import hashlib
import time
import json

def block(proof,previous_hash=None):
	transaction={
	"Sender" : "Heena"
	"Receiver" : "Ziyah"
	"amount" : '5 ETH'
	}
	data={
	'block_height' : 12913586,
	'timestamp': time(),
	'transactions' : transaction,
	'Block Reward' :2.557309540563,
	'Uncle Reward' :6598,
	'Difficulty' :7317161775076869,
	'Total Difficulty' :0.1,
	'Size' :0.1,
	'Gas Used' :0.1,
	'Gas Limit' :0.1,
	'proof' : proof,
	'previous_hash': previous_hash
	}
	chain.append(data)
	print("Block Info: ", data)
	jobject = json.dumps(data)
	eobject = jobject.encode()

	raw_hash = hashlib.sha512(eobject)
	hex_hash = raw_hash.hexdigest()
	print("Hash of Block: " ,hex_hash)

block(previous_hash="No previous Hash. Since this is the first block.",proof=000)



