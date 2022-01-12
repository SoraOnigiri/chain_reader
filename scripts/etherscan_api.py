"""
Etherscan API - The following takes an address as input and returns all of the transactions logged by etherscan for that address. 
Etherscan categorizes transactions into 4 different groups: 
    1. Normal Transactions 
    2. Internal Transactions 
    3. ERC20 Token Transactions 
    4. ERC721 Token Transactions 
    *note* ERC1155 Token Transactions are multi-token transactions and are logged as separate transactions under category 3. ERC20 Token Transactions.
"""

import json
import requests
import time


def get_normal_transactions(address, startblock, endblock, apikey):
    print("Processing Normal Transactions...")
    module = "account"
    action = "txlist"
    page = 1
    index = 1
    offset = "1000"
    result = []
    quit = False
    while quit == False:
        if quit == False:
            r = requests.get(
                f"https://api.etherscan.io/api?module={module}&action={action}&address={address}&startblock={startblock}&endblock={endblock}&page={str(page)}&offset={offset}&sort=asc&apikey={apikey}"
            )
            if r.json()["status"] == "1":
                result.append(r.json()["result"])
                print(f"processed page {index}.")
                page += 1
                index += 1
                if page == 11:
                    page = 1
                    startblock = r.json()["result"][-1]["blockNumber"]
            else:
                quit = True
                print(r.json()["message"])

    return result


def get_internal_transactions(address, startblock, endblock, apikey):
    print("Processing Internal Transactions...")
    module = "account"
    action = "txlistinternal"
    page = 1
    offset = "1000"
    result = []
    index = 1
    quit = False
    while quit == False:
        if quit == False:
            r = requests.get(
                f"https://api.etherscan.io/api?module={module}&action={action}&address={address}&startblock={startblock}&endblock={endblock}&page={str(page)}&offset={offset}&sort=asc&apikey={apikey}"
            )
            if r.json()["status"] == "1":
                result.append(r.json()["result"])
                print(f"processed page {index}.")
                page += 1
                index += 1
                if page == 11:
                    page = 1
                    startblock = r.json()["result"][-1]["blockNumber"]
            else:
                quit = True
                print(r.json()["message"])

    return result


def get_erc20_transactions(address, startblock, endblock, apikey):
    print("Processing Token Transactions...")
    module = "account"
    action = "tokentx"
    page = 1
    index = 1
    offset = "1000"
    result = []
    quit = False
    while quit == False:
        if quit == False:
            r = requests.get(
                f"https://api.etherscan.io/api?module={module}&action={action}&address={address}&startblock={startblock}&endblock={endblock}&page={str(page)}&offset={offset}&sort=asc&apikey={apikey}"
            )
            if r.json()["status"] == "1":
                result.append(r.json()["result"])
                print(f"processed page {index}.")
                page += 1
                index += 1
                if page == 11:
                    page = 1
                    startblock = r.json()["result"][-1]["blockNumber"]
            else:
                quit = True
                print(r.json()["message"])

    return result


def get_erc721_transactions(address, startblock, endblock, apikey):
    print("Processing NFT Transactions...")
    module = "account"
    action = "tokennfttx"
    page = 1
    offset = "1000"
    result = []
    index = 1
    quit = False
    while quit == False:
        if quit == False:
            r = requests.get(
                f"https://api.etherscan.io/api?module={module}&action={action}&address={address}&startblock={startblock}&endblock={endblock}&page={str(page)}&offset={offset}&sort=asc&apikey={apikey}"
            )
            if r.json()["status"] == "1":
                result.append(r.json()["result"])
                print(f"processed page {index}.")
                page += 1
                index += 1
                if page == 11:
                    page = 1
                    startblock = r.json()["result"][-1]["blockNumber"]
            else:
                quit = True
                print(r.json()["message"])

    return result


def retrieve_account_transactions(address, apikey, start):

    end = str(int(time.time()))
    block_range = get_block_range(start, end, apikey)
    normal_tx = get_normal_transactions(address, block_range[0], block_range[1], apikey)
    internal_tx = get_internal_transactions(
        address, block_range[0], block_range[1], apikey
    )
    erc20_tx = get_erc20_transactions(address, block_range[0], block_range[1], apikey)
    erc721_tx = get_erc721_transactions(address, block_range[0], block_range[1], apikey)
    return [normal_tx, internal_tx, erc20_tx, erc721_tx]


def get_block_range(start, end, apikey):
    if start == "0":
        start_block = 1
    else:
        start_block = requests.get(
            f"https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp={start}&closest=before&apikey={apikey}"
        ).json()["result"]
    end_block = requests.get(
        f"https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp={end}&closest=before&apikey={apikey}"
    ).json()["result"]
    return (start_block, end_block)
