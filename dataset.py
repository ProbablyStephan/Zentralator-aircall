import csv
import os

data = [["stephan.rott","1054671","DEV"],
        ["igor.dymler","983875","DEV"],
        ["thomas.krieninger","1055361","SP"],
        ["benjamin.sueffert","1055315","SP"],
        ["nadege.viaud","1055322","TSR"],
        ["driton.kola","1055360","TSR"],
        ["ferdinand.herrmann","1055349","TSR"],
        ["horst.sueffert","1055313","TSR"],
        ["anja.maerz","1055366","CSR"],
        ["julia.schwaiger","1055277","CSR"],
        ["katrin.loeffler","1055277","CSR"],
        ["marina.weweck","1055331","CSR"],
        ["markus.croseck","1055334","CSR"],
        ["christian.herrmann","1055346","CSR"]]


#Funktionen Liste
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
