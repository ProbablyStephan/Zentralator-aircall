# mapping of the list
# windows account name - aircall ID - Department

# Improvement: checking if the network file can be opened. If not we use backup data implemented as variable (only viable if the data set is small) 
# Ensures functionality of the programm.  
# If new members get added it still reults in new compilation and distribution.
data = None


backupData = [["user1","aircall_ID1","Department"],
        ["user2","aircall_ID2","Department"],
        ["user3","aircall_ID3","Department"]]


	

#dataset functions
def loadFile():
    try:
        csvfile = open(r"Full Qualified Name of the filelocation", newline="")
        return list(csv.reader(csvfile,delimiter=",")) , "Network File Used"
    except:
        return backupData, "Backup Data Used"

def inList(name):
    for x in data:
        if x[0] == name:
            return True
        else:
            tmp = False
    return tmp

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
