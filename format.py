import pandas as pd

data = pd.read_csv("final.csv")

print(data["Joined"])

def getMY(date):
    res = date.split(" ")[0].split("-")
    return res[1] + "/" + res[0][2:4]

data["Joined"] = list(map(getMY, list(data["Joined"])))

print(data)

data.to_csv('nFinal.csv', index=False)


