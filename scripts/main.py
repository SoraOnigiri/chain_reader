from settings import *
from etherscan_api import *
from reformat import *
import json

apikey = os.getenv("APIKEY")


def create_account(path, address):
    os.makedirs(path)
    os.makedirs(path + "/jsontx/")
    os.makedirs(path + "/csvtx/")


Continue = True
while Continue == True:

    function = input("What would you like to do? \n")

    if function == "quit":
        Continue = False
        print("\nGood Bye!\n")
    elif function == "help":
        print("\nFunctions:\n'transactions'\n")
    elif function == "transactions":
        again = True
        while again == True:
            # Grab all transactions by the user.
            address = input("Please input an Eth Address: ")
            start = input("Please input a start timestamp: ")
            transactions = retrieve_account_transactions(address, apikey, start)
            path = f"../database/addresses/{address}"
            if not os.path.exists(path):
                # os.makedirs(path)
                create_account(path, address)
                print(f"New path: {path}")
            path = path + "/jsontx/"
            with open(f"{path}_normaltx.json", "w") as outfile:
                json.dump(transactions[0], outfile)
            with open(f"{path}_internaltx.json", "w") as intx:
                json.dump(transactions[1], intx)
            with open(f"{path}_erc20tx.json", "w") as erc20tx:
                json.dump(transactions[2], erc20tx)
            with open(f"{path}_erc721tx.json", "w") as erc721tx:
                json.dump(transactions[3], erc721tx)
            repeat = input("Would you like to input another Eth Address? 'y'es|'n'o")
            if repeat == "n":
                again = False
    elif function == "format_tx":
        address = input("Please input an Eth Address: ")
        path = f"../database/addresses/{address}"
        if not os.path.exists(path):
            print("Address is not in the database.\n")
        else:
            reformat_normal_tx(address, path)

    else:
        print("\nNot a valid function. Input 'help' for more information.\n")
