#to hide the API Token its saved in a user enviromental variable (rolled out to machines via GPO)
#


import os

def getHeaderLocal():
    tmp = "Basic " + os.environ.get("NAME OF VARIABLE")
    return {"Authorization": tmp, "Content-Type": "application/json"}
