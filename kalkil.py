from scicalculator import add, division, soustraction, multipy
from kalkilatris_syantifik import square, exponentiel, factoriel

a=0
b=0
rezilta=0

def adisyone():
    a=input("rantre premye nonb lan: ")
    b=input("rantre dezyem nonb lan: ")
    rezilta=add(a,b)
    print(f"rezilta operasyon ou an se {rezilta}")
    return rezilta
    

def soustre():
    a=input("rantre premye nonb lan: ")
    b=input("rantre dezyem nonb lan: ")
    rezilta=soustraction(a,b)
    print(f"rezilta operasyon ou an se {rezilta}")
    return rezilta

def miltiplikasyon():
    a=input("rantre premye nonb lan: ")
    b=input("rantre dezyem nonb lan: ")
    rezilta=multipy(a,b)
    print(f"rezilta operasyon ou an se {rezilta}")
    return rezilta


def divizyon():
    a=input("rantre premye nonb lan: ")
    b=input("rantre dezyem nonb lan: ")
    rezilta=soustraction(a,b)
    print(f"rezilta operasyon ou an se {rezilta}")
    return rezilta


def kalkileRasinn():
    a=input("rantre  nonb lan: ")
    rezilta=square(a)
    print(f"rezilta operasyon ou an se {rezilta}")



def kalkilFaktoryel():
    a=input("rantre  nonb lan: ")
    rezilta=factoriel(a)
    print(f"rezilta operasyon ou an se {rezilta}")



def kalkilExpo():
    a=input("rantre  nonb lan: ")
    rezilta=exponentiel(a)
    print(f"rezilta operasyon ou an se {rezilta}")