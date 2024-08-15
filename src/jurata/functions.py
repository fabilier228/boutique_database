from datetime import datetime
import json

def existsObject(parameter, value, obTab):
    for i in obTab:
        if i[parameter] == value:
            return True
    return False

def updateDataBase(fileName):
    with open("db.json", "r") as current:
        data = json.load(current)

    with open("db_previous.json", "w") as previous:
        json.dump(data, previous, indent=4)

    with open(f"data/dostawy/{fileName}.csv", "r") as file:
        readableFile = file.read().strip().split("\n")

    for line in readableFile:
        name, count = line.split(",")
        count = int(count)
        if existsObject("nazwa", name, data):
            for item in data:
                if item["nazwa"] == name:
                    item["ilosc"] += count
                    item["ostatniaZmiana"] = str(datetime.now())
        else:
            data.append({"nazwa": name, "ilosc": count, "ostatniaZmiana": str(datetime.now())})

    with open("db.json", "w") as currentWrite:
        json.dump(data, currentWrite, indent=4)



def takings(fileName):
    with open("db.json", "r") as current:
        data = json.load(current)

    with open(f"data/utarg/{fileName}.csv", "r") as file:
        readableFile = file.read().split("\n")

    money = 0
    for product in readableFile:
        name, price = product.split(",")
        price = float(price)
        for item in data:
            if item["nazwa"] == name:
                item["ilosc"] -= 1
        money += price

    with open("db.json", "w") as currentWrite:
        json.dump(data, currentWrite, indent=4)

    print(f"Dzisiejszy utarg wynosi: {money}")

def printOutState():
    with open("db.json", "r") as current:
        data = json.load(current)

    text = open("test.txt", "w")

    for i in data:
        text.write(f"Produktu {i["nazwa"]} jest {i["ilosc"]}")
        text.write("\n")


printOutState()


