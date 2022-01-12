import json
import csv
import pandas as pd

# with open("transaction.json", "r") as tx:
#     transactions = json.load(tx)

# "blockNumber": "11565033",
# "timeStamp": "1609459363",
# "hash": "0x2a4aa907ecd466d3e7cabe7b0f342c5c6a4ab05dbd4429293d7cd974569d29a2",
# "nonce": "1053",
# "blockHash": "0x93a27737874c6c07b5c04081fcfddbfa10a49ca729a437e9eecb4fe5cc554897",
# "from": "0xd8025919d61898ecf920643c8f773c93b2839753",
# "contractAddress": "0x2b591e99afe9f32eaa6214f7b7629768c40eeb39",
# "to": "0x55d5c232d921b9eaa6b37b5845e439acd04b4dba",
# "value": "25257148654036",
# "tokenName": "HEX",
# "tokenSymbol": "HEX",
# "tokenDecimal": "8",
# "transactionIndex": "119",
# "gas": "154944",
# "gasPrice": "69000000000",
# "gasUsed": "100577",
# "cumulativeGasUsed": "5555149",
# "input": "deprecated",
# "confirmations": "2286484"

# data = "Block Number, Time Stamp, Hash, Nonce, Block Hash, From, Contract Address, To Address, Value, Token Name, Token Symbol, Token Decimal, Transaction Index, Gas, Gas Price, Gas Used, Cumulative Gas Used\n"

# for i in transactions:
#     data = data + i["blockNumber"] + "," + i["timeStamp"] + "," + i["hash"] + "," + i["nonce"] + "," + i["blockHash"] + "," + i["from"] + "," + i["contractAddress"] + "," + i["to"] + "," + \
#         i["value"] + "," + i["tokenName"] + "," + i["tokenSymbol"] + "," + i["tokenDecimal"] + "," + i["transactionIndex"] + "," + \
#         i["gas"] + "," + i["gasPrice"] + "," + \
#         i["gasUsed"] + "," + i["cumulativeGasUsed"] + "\n"

# file1 = open("log.csv", "w")
# file1.write(data)
# file1.close()

# module = "account"
# action = "tokentx"
# fromBlock = 11565026
# toBlock = 13850412
# address = "0xd8025919d61898ecf920643c8f773c93b2839753"
# contractAddress = "0xe592427a0aece92de3edee1f18e0157c05861564"
# r = requests.get(
#     f'https://api.etherscan.io/api?module={module}&action={action}&address={address}&startblock={fromBlock}&endblock={toBlock}&sort=asc&apikey={apikey}')

# with open("transaction.json", "w") as outfile:
#     json.dump(r.json()["result"], outfile)
#     print("internal transaction saved")

# with open("transaction.json", "r") as tx:
#     transactions = json.load(tx)

# # transaction is an array of transactions
# # create a dict of arrays to pair all of the transactions together
# # logix, if dict does not exist, add empty array and then start appending
# dtx = {}

# for i in transactions:
#     if i["hash"] not in dtx:
#         dtx[i["hash"]] = []
#         dtx[i["hash"]].append(i)
#     else:
#         dtx[i["hash"]].append(i)

# with open("results.json", "w") as outfile:
#     json.dump(dtx, outfile)
#     print("results completed.")

# r = requests.get(
#     f"https://api.etherscan.io/api?module=account&action=tokentx&address=0xd8025919d61898ecf920643c8f773c93b2839753&page=1&offset=100&startblock=13809615&endblock=13809615&sort=asc&apikey={apikey}")
# with open("ethscan.json", "w") as outfile:
#     json.dump((r.json()["result"]), outfile)
#     print("results completed.")

# r = requests.get(
#     f"https://api.etherscan.io/api?module=account&action=txlistinternal&txhash=0xc3b90a086fdfd686e1f43187707a8ba83707b7a41070d292a399c669d8d939be&apikey={apikey}")
# with open("ethscan.json", "w") as outfile:
#     json.dump((r.json()), outfile)
#     print("results completed.")

# &txhash=0xc3b90a086fdfd686e1f43187707a8ba83707b7a41070d292a399c669d8d939be
# csvfile = open("0xd8025919d61898ecf920643c8f773c93b2839753.csv", newline='')
# c = csv.reader(csvfile)
# header = next(c)
# data = {}
# data["header"] = header
# for transaction in c:
#     if transaction[0] not in data:
#         data[transaction[0]] = []
#     data[transaction[0]].append(transaction)


# with open("result.json", "w") as outfile:
#     json.dump(data, outfile)
#     print("transactions logged.")

# ==================== IMPORT CSV ======================


# convert = {}
# with open("download.csv",  "r") as csvfile:
#     c = csv.reader(csvfile, delimiter=',')
#     next(c)

#     for row in c:
#         if row[0] not in convert:
#             convert[row[0]] = []
#             template = {"txhash": row[0],
#                         "block": row[1],
#                         "unixtime": row[2],
#                         "from": row[4],
#                         "to": row[5],
#                         "txfeeeth": row[10],
#                         "txfeeusd": row[11],
#                         "historicaleth": row[12],
#                         "method": row[15]}
#             convert[row[0]].append(template)


# with open("convert.json", "w") as outfile:
#     json.dump(convert, outfile)
#     print("conversion complete.")

# =======================================================

# with open('convert.json', "r") as outfile:
#     c = json.load(outfile)

# =======================================================

# module = "account"
# action = "txlistinternal"
# address = "0x19234EC8d2e3C8726beB0456c109bd8F238e0039"
# contractAddress = ""
# txhash = "0xd25e54ff5efb797530b1d4f195a21f3de649ad310bd9fed54cd734178fc10a31"
# startblock = "0"
# endblock = "99999999"
# page = "1"
# offset = "10"
# sort = "asc"


# r = requests.get(
#     f"https://api.etherscan.io/api?module=account&action=txlistinternal&txhash=0xc3b90a086fdfd686e1f43187707a8ba83707b7a41070d292a399c669d8d939be&apikey={apikey}")
# with open("ethscan.json", "w") as outfile:
#     json.dump((r.json()), outfile)
#     print("results completed.")

# r = requests.get(
#     f"https://api.etherscan.io/api?module={module}&action={action}&txhash={txhash}&apikey={apikey}")

# with open("internaltxhash.json", "w") as outfile:
#     json.dump(r.json(), outfile)
#     print("Got data.")


def geterc20(_apikey, _start_block, _end_block, _address):
    #     https://api.etherscan.io/api
    #    ?module=account
    #    &action=tokentx
    #    &contractaddress=0x9f8f72aa9304c8b593d555f12ef6589cc3a579a2
    #    &address=0x4e83362442b8d1bec281594cea3050c8eb01311c
    #    &page=1
    #    &offset=100
    #    &startblock=0
    #    &endblock=27025780
    #    &sort=asc
    #    &apikey=YourApiKeyToken
    module = "account"
    action = "tokentx"
    sort = "desc"
    r = requests.get(
        f"https://api.etherscan.io/api?module={module}&action={action}&address={_address}&startblock={_start_block}&endblock={_end_block}&sort={sort}&apikey={_apikey}"
    )
    return r.json()["result"]


def geterc721():
    pass


# with open("convert.json", "r") as data:
#     c = json.load(data)

# convert = []
# for i in c:
#     convert.append(i)

# start_block = c[convert[0]][0]["block"]
# end_block = c[convert[-1]][0]["block"]
apikey = os.getenv("APIKEY")
# address = "0xd8025919d61898Ecf920643C8f773c93B2839753"

# erc20_data = geterc20(apikey, start_block, end_block, address)

# # with open("erc20.json", "w") as outfile:
# #     json.dump(erc20_data, outfile)
# #     print("erc20 information retrieved.")

# test = {}
# print(len(erc20_data))
# for erc in erc20_data:
#     if erc["hash"] not in test:
#         test[erc["hash"]] = []
#     test[erc["hash"]].append(erc)

# with open("test.json", "w") as outfile:
#     json.dump(test, outfile)

# etherscan.json holds all transactions
# crossreference test.json with etherscan.json to build list of missing transaction hashes


# with open("test.json", "r") as test:
#     t = json.load(test)

# with open("convert.json", "r") as data:
#     c = json.load(data)

# txlist = []
# for tx in c:
#     if tx not in t:
#         txlist.append(tx)


def getStatus(txhash, apikey):
    r = requests.get(
        f"https://api.etherscan.io/api?module=transaction&action=getstatus&txhash={txhash}&apikey={apikey}"
    )
    return r.json()["result"]["isError"]


# errorlist = []
# validlist = []

# with open("missing.json", "r") as missing:
#     m = json.load(missing)

# for i in m:
#     s = getStatus(i, apikey)
#     if s == '0':
#         validlist.append(i)
#     elif s == '1':
#         errorlist.append(i)

# with open("error.json", "w") as err:
#     json.dump(errorlist, err)

# with open("valid.json", "w") as val:
#     json.dump(validlist, val)

# # print(len(errorlist))
# # print(len(validlist))

# with open("test.json", "r") as test:
#     t = json.load(test)

# with open("convert.json", "r") as data:
#     c = json.load(data)

# c2t = []
# for tx in c.keys():
#     if tx not in t:
#         c2t.append(tx)

# t2c = []
# for tx in t:
#     if tx not in c.keys():
#         t2c.append(tx)


# # with open("t2c.json", 'w') as outfile:
# #     json.dump(t2c, outfile)

# print(len(c2t))
# print(len(t2c))


import json
import csv

# function to separate the transactions between sales and purchases:


def sort_transactions(transactions, address):
    sales = []
    purchases = []
    for k, v in transactions.items():
        if v[0]["to"] == address:

            purchases.append({k: v})
        elif v[0]["from"] == address:
            sales.append({k: v})
    with open("purchase_normal.json", "w") as p:
        json.dump(purchases, p)
    with open("sales_normal.json", "w") as s:
        json.dump(sales, s)
    print(len(transactions))
    print(len(sales))
    print(len(purchases))
    print(len(sales + purchases))


address = "0x6bddbd1d6bbe36aff9a1dff1e4067148425a76d9"
with open("cnormaltx.json", "r") as data:
    tx = json.load(data)

sort_transactions(tx, address)
