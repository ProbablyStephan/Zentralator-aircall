import requests
import secret
import os
import list


def safeGuard():
    r = requests.get("URL of Aircall API - team",headers=secret.getHeaderLocal())
    data = r.json()
    if len(data["team"]["users"]) > 5:
        return True
    else:
        return False

def teamCheck():
    response = requests.get("URL of Aircall API - team",headers=secret.getHeaderLocal())
    data = response.json()
    if response.status_code == 200:
        for x in data["team"]["users"]:
            if str(x["id"]) == list.getID(os.environ.get("Username")):
                return os.environ.get("Username") + " ist in Zentrale"
            else:
                return os.environ.get("Username") + " ist nicht in Zentrale"
    elif response.status_code == 400:
        return "400 - Bad Request"
    elif response.status_code == 403:
        return "403 - Forbidden"
    elif response.status_code == 404:
        return "404 - Target Resource not found"
    elif response.status_code == 405:
        return "405 - Method Not Allowed"
    else:
        return response

def teamPost():
    userID = list.getID(os.environ.get("Username")) 
    apiURL ="URL of Aircall API - team/users"+userID

    response = requests.post(apiURL,headers=secret.getHeaderLocal())
    if response.status_code == 200:
        return "200 - OK"
    elif response.status_code == 201:
        return os.environ.get("Username") + " jetzt in Zentrale"
    elif response.status_code == 400:
        return "400 - Bad Request"
    elif response.status_code == 403:
        return "403 - Forbidden"
    elif response.status_code == 404:
        return "404 - Target Resource not found"
    elif response.status_code == 405:
        return "405 - Method Not Allowed"
    elif response.status_code == 422:
        return os.environ.get("Username") + " bereits in Zentrale"
    else:
        return response

def teamDelete():
    userID = list.getID(os.environ.get("Username")) 
    apiURL ="URL of Aircall API - team/users"+userID

    response = requests.delete(apiURL,headers=secret.getHeaderLocal())
    if response.status_code == 200:
        return os.environ.get("Username") + " aus Zentrale"
    elif response.status_code == 400:
        return "400 - Bad Request"
    elif response.status_code == 403:
        return "403 - Forbidden"
    elif response.status_code == 404:
        return "404 - Target Resource not found"
    elif response.status_code == 405:
        return "405 - Method Not Allowed"
    else:
        return response
    
def guardedDelete():
    if safeGuard():
        tmp = teamDelete()
        return tmp
    else:
        return "Verboten - zu wenig Mitgieder in Zentrale"
