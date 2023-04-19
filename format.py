import pandas as pd
from datetime import datetime

data = pd.read_csv("data_pt2.csv")

def getMY(date):
    res = date.split(" ")[0].split("-")
    return res[1] + "/" + res[0][2:4]

def getCT(ct):
    print(ct)
    if ct[0] == " ":
        res = ct[1:]
    res = res.replace(" ",",")
    return res




    

# data = data[(data.FLAG == "ACCEPT") & (data.Timestamp < "4/1/2023 12:27:59")]
# data.to_csv('test.csv', index=False)
# print(data["Content type"])
# data["Joined"] = list(map(getMY, list(data["Joined"])))
# data["Content type"] = list(map(getCT, list(data["Content type"])))
# print(data["Joined"])

def getDP(dd):
    a = dd.split(" ")
    date = a[0].split("/")
    time = a[1].split(":")
    time[0] = int(time[0])+8

    if time[0] > 24:
        date[1] = str(int(date[1])+1)
        time[0] = time[0] - 24
    
    return date[0] + "/" + date[1] + "/" + date[2] + " " + str(time[0]) + ":" + time[1]


data["Date posted"] = list(map(getDP, list(data["Date posted"])))

data.to_csv('data_pt2_new.csv', index=False)


