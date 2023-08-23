import csv
import os

# mapping of the list
# windows account name to aircall ID 


# two possibilities to access the mapping list of user to aircall ID.
# 1. list as variable
data = [["user1","aircall_ID1"],
        ["user2","aircall_ID2"],
        ["user3","aircall_ID3"]]

# 2. open a .csv on a networkdrive. (possible problems when using over VPN)
with open(r"Full Qualified Name of the filelocation", newline="") as csvfile:
    data = list(csv.reader(csvfile,delimiter=","))

def getID(name):
    for x in data:
        if x[0] == name:
            return x[1]
        else:
            tmp = "User not in List"
    return tmp
