import requests
import secret
import os
import dataset

currentUser = ""

def initUser():
    return os.environ.get("Username")
    
#API calls

def teamCheck(name):
    try:
        r = requests.get("Aircall API URL - team",headers=secret.getHeaderLocal())
        if r.status_code == 200:
            for x in r.json()["team"]["users"]:
                if str(x["id"]) == dataset.getID(name):
                    return f'{name} ist in Zentrale.'
                else:
                    return f'{name} ist nicht in Zentrale.'
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        return errh
    except requests.exceptions.ConnectionError as errc:
        return errc
    except requests.exceptions.Timeout as errt:
        return errt
    except requests.exceptions.RequestException as err:
        return err

def addToTeam(name):
    try:
        apiURL = "Aircall API URL - users"+dataset.getID(name)
        r = requests.post(apiURL,headers=secret.getHeaderLocal())
        if r.status_code == 201:
            return f'{name} ist Zentrale beigetreten.'
        elif r.status_code == 422:
            return f'{name} ist bereits in Zentral.'
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        return errh
    except requests.exceptions.ConnectionError as errc:
        return errc
    except requests.exceptions.Timeout as errt:
        return errt
    except requests.exceptions.RequestException as err:
        return err
    
def removeFromTeam(name):
    try:
        apiURL = "Aircall API URL - users"+dataset.getID(name)
        r = requests.delete(apiURL,headers=secret.getHeaderLocal())
        if r.status_code == 200:
            return f'{name} hat Zentrale verlassen.'
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        return errh
    except requests.exceptions.ConnectionError as errc:
        return errc
    except requests.exceptions.Timeout as errt:
        return errt
    except requests.exceptions.RequestException as err:
        return err
    
def listMembers():
    try:
        r = requests.get("Aircall API URL - team",headers=secret.getHeaderLocal())
        if r.status_code == 200:
            tmp = []
            for x in r.json()["team"]["users"]:
                tmp.append(x["name"])
            return tmp
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        return errh
    except requests.exceptions.ConnectionError as errc:
        return errc
    except requests.exceptions.Timeout as errt:
        return errt
    except requests.exceptions.RequestException as err:
        return err
        
def getZentraleIDs():
    try:
        r = requests.get("Aircall API URL - team",headers=secret.getHeaderLocal())
        if r.status_code == 200:
            tmp = []
            for x in r.json()["team"]["users"]:
                tmp.append(x["id"])
            return tmp
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        return errh
    except requests.exceptions.ConnectionError as errc:
        return errc
    except requests.exceptions.Timeout as errt:
        return errt
    except requests.exceptions.RequestException as err:
        return err

#Logic

def safeGuard():
    try:
        r = requests.get("Aircall API URL - team",headers=secret.getHeaderLocal())
        if len(r.json()["team"]["users"]) > 5:
            return True
        elif len(r.json()["team"]["users"]) <= 5:
            return False
        r.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        return errh
    except requests.exceptions.ConnectionError as errc:
        return errc
    except requests.exceptions.Timeout as errt:
        return errt
    except requests.exceptions.RequestException as err:
        return err

def complexGuard(name):
    match dataset.getDep(name):
        case "DEV":
            return True 
        case "SP":
            return True
        case "VI":
            return True
        case "CSR":                
            if sum(str(x) in dataset.listMember("CSR") for x in getZentraleIDs()) >= 3:
                return True
            else:
                return False
        case "TSR":
            if sum(str(x) in dataset.listMember("TSR") for x in getZentraleIDs()) >= 2:
                return True
            else:
                return False
        case _:
            return "unknown user"

def complexeDelete(name):
    if complexGuard(name) == True:
        return removeFromTeam(name)
    elif complexGuard(name) == False:
        return "!!! Zu wenig Mitarbeiter in Zentrale !!!"
    else:
        return f'Guard: {str(complexGuard(name))}'
