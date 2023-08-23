# according to aircall guidelines:
# The Authorization HTTP header is constructed as follows:
# The api_id and api_token are concatenated with a single colon :.
# The resulting string is encoded using Base64.
# The authorization header results in Authorization: Basic YOUR_ENCODED_STRING

#the encoded string is saved in a user enviroment variable (rolled out to machines via GPO)
import os

def getHeaderLocal():
    tmp = "Basic " + os.environ.get("NAME OF VARIABLE")
    return {"Authorization": tmp, "Content-Type": "application/json"}


#or in a system enviroment variable
import winreg

def getHeader():
    reg_path = r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment'
    reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path)
    system_environment_variables = winreg.QueryValueEx(reg_key, 'NAME OF VARIABLE')[0]
    tmp = "Basic " + system_environment_variables 
    return {"Authorization": tmp, "Content-Type": "application/json"}
