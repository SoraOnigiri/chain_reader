import json

"""
{"blockNumber": "5339404", 
"timeStamp": "1522274054", 
"hash": "0xd76f3b3073fcb450fe8eb6c47028b2c5365e94dfab4b31e5fd5ba09f29be2a46", 
"nonce": "0", 
"blockHash": "0x8fb1a74f6e7c5b94bc379a5922df8f5ca0d10f7761e49c2adf2a85d700379cd3", 
"transactionIndex": "58", 
"from": "0x7ec3df315d938f64090a575a6d4bd269f5527c3b", 
"to": "0x6bddbd1d6bbe36aff9a1dff1e4067148425a76d9", 
"value": "4999895000000000000", 
"gas": "21000", 
"gasPrice": "5000000000", 
"isError": "0", 
"txreceipt_status": "1", 
"input": "0x", 
"contractAddress": "", 
"cumulativeGasUsed": "1896232", 
"gasUsed": "21000", 
"confirmations": "8615242"}
"""
# Pages -> 1000tx -> tx
def reformat_normal_tx(address, path):
    path = path + "/jsontx/_normaltx.json"
    print(path)
    with open(path, "r") as ntx:
        newtx = json.load(ntx)
        csvfile = ""
        for page in newtx:
            for tx in page:
                blockNumber = tx["blockNumber"]
                timeStamp = tx["timeStamp"]
                txhash = tx["hash"]
                nonce = tx["nonce"]
                blockHash = tx["blockHash"]
                transactionIndex = tx["transactionIndex"]
                txfrom = tx["from"]
                txto = tx["to"]
                value = tx["value"]
                gas = tx["gas"]
                gasPrice = tx["gasPrice"]
                isError = tx["isError"]
                txreceipt_status = tx["txreceipt_status"]
                txinput = tx["input"]
                contractAddress = tx["contractAddress"]
                cumulativeGasUsed = tx["cumulativeGasUsed"]
                gasUsed = tx["gasUsed"]
                confirmations = tx["confirmations"]
                csvfile = csvfile + blockNumber + "," + timeStamp + "," txhash + "," nonce + "," blockHash + "," transactionIndex + "," txfrom + "," txto + "," value + "," gas + "," gasPrice + "," isError + "," txreceipt_status + "," txinput + "," contractAddress + "," cumulativeGasUsed + "," gasUsed + "," confirmations + "\n"


def reformat_internal_tx(address, path):
    pass


def reformat_erc20_tx(address, path):
    pass


def reformat_erc721_tx(address, path):
    pass


def reformat(address):
    path = f"../database/addresses/{address}/tx"
    reformat_normal_tx()
    reformat_internal_tx()
    reformat_erc20_tx()
    reformat_erc721_tx()
