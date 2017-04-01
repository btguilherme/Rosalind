# -.- encoding:utf-8 -.-
import sys

def verifySum(a,b,c):
    soma = a + b + c
    if soma < 2:
        print "Soma dos indivíduos deve ser >= 2 (evitar divisão por zero)."
        sys.exit(0)
    return

def verifyPositivity(a,b,c):
    if (a < 0) or (b < 0) or (c < 0):
        print "Parâmetros de entrada devem ser positivos."
        sys.exit(0)
    return

def verifyNumber(a,b,c):
    try:
        aa = int(a)
        bb = int(b)
        cc = int(c)
    except ValueError as e:
        print "Parâmetros de entrada devem ser inteiros positivos."
        sys.exit(0)
    else:
        pass
