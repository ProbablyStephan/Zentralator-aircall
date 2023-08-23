import csv
import os


data = [["thomas.krieninger","1055361"],
        ["stephan.rott","1054671"],
        ["igor.dymler","983875"],
        ["anja.maerz","1055366"],
        ["christian.herrmann","1055346"],
        ["driton.kola","1055360"],
        ["ferdinand.herrmann","1055349"],
        ["horst.sueffert","1055313"],
        ["julia.schwaiger","1055277"],
        ["katrin.loeffler","1055277"],
        ["marina.weweck","1055331"],
        ["markus.croseck","1055334"],
        ["nadege.viaud","1055322"],
        ["benjamin.sueffert","1055315"]]


def getID(name):
    for x in data:
        if x[0] == name:
            return x[1]
        else:
            tmp = "User not in List"
    return tmp
