import json

with open("normaltx.json", "r") as normaltx:
    data = json.load(normaltx)

pages = len(data)
transactions = (pages - 1) * 1000 + len(data[-1])
print(transactions)
