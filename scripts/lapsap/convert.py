import json

# [
#     [
#         {
#             "blockNumber": "11565364",
#             "timeStamp": "1609463747",
#             "hash": "0x84d7dbc9c3676a61fe022c6d826621d0ab1d0d26b5453749a3b068aac3a3d9d4",
#             "nonce": "33742",
#             "blockHash": "0xf9d890fdc5d75884f02b4af70f28564d4d44d93faeea2c34c087866964c8b40b",
#             "transactionIndex": "80",
#             "from": "0x6bddbd1d6bbe36aff9a1dff1e4067148425a76d9",
#             "to": "0x0891cc1fa5cddb6c2a18ad83553e354e34bd103c",
#             "value": "287790454939369440",
#             "gas": "46200",
#             "gasPrice": "98475001312",
#             "isError": "0",
#             "txreceipt_status": "1",
#             "input": "0x",
#             "contractAddress": "",
#             "cumulativeGasUsed": "4161397",
#             "gasUsed": "21000",
#             "confirmations": "2349036"
#         },
with open("normaltx.json", "r") as normaltx:
    ntx = json.load(normaltx)

length = len(ntx)
newntx = {}

for i in range(length):
    for transaction in ntx[i]:
        if transaction["hash"] not in newntx:
            newntx[transaction["hash"]] = []
            newntx[transaction["hash"]].append(transaction)
        else:
            newntx[transaction["hash"]].append(transaction)

with open("cnormaltx.json", "w") as outfile:
    json.dump(newntx, outfile)


# with open("cnormaltx.json", "r") as data:
#     new = json.load(data)
