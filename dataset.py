# mapping of the list
# windows account name - aircall ID - Department


# two possibilities to access the mapping list of user to aircall ID.
# 1. list as variable
data = [["user1","aircall_ID1","Department"],
        ["user2","aircall_ID2","Department"],
        ["user3","aircall_ID3","Department"]]

# 2. open a .csv on a networkdrive. (possible problems when using over VPN)
with open(r"Full Qualified Name of the filelocation", newline="") as csvfile:
    data = list(csv.reader(csvfile,delimiter=","))
	

#dataset functions
def getID(name):
    for x in data:
        if x[0] == name:
            return x[1]
        else:
            tmp = "unknown user"
    return tmp

def getDep(name):
    for x in data:
        if x[0] == name:
            return x[2]
        else:
            tmp = "unknown user"
    return tmp
