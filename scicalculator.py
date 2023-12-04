

def add(a,b):
    a=int(a)
    b=int(b)
    resulta=a+b

    return resulta


def soustraction(a,b):
    a=int(a)
    b=int(b)
    resulta= a-b
    return resulta


def multipy(a,b):
    a=int(a)
    b=int(b)
    resulta= a*b

    return resulta



def division(a,b):
    a=int(a)
    b=int(b)
    try:
        a !=0 or b !=0
        resulta= float(a/b)
        return resulta
    except ZeroDivisionError:
        print("ou paka fe divizyon ak 0")
        return None