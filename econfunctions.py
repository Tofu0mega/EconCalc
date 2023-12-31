import math


def FV(k, n):
    val = (1 + (k / 100)) ** n
    return round(val, 5)


def PV(k, n):
    val = (1 + (k / 100)) ** (0 - n)
    return round(val, 5)


def FVA(k, n):
    val = (((1 + k / 100) ** n) - 1) / (k / 100)
    return round(val, 5)


def PVA(k, n):
    val = (1 - ((1 + k / 100) ** (0 - n))) / (k / 100)
    return round(val, 5)

def AER(k,n):
    i=k/100
    val=((1+k/n)**n)-1
    return round(val,5)

def help():
    msg="Available Functions :\n FV(k,n),PV(k,n),FVA(k,n),PVA(k,n),AER(k,n)\n UseExample(For future value of initial payment of 1000 with 200 annuity after 5 years at 10%:1000*FV(10,5)+200*FVA(10,5)"
    return msg