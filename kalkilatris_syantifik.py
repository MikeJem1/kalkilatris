

def square(a):
    a=int(a)
    
    if a >=0:
        resulta=a**0.5
        return resulta
    else:
        print(" non ou chwazi a pi piti ke 0")
        return None
    

def exponentiel(a):
    a=int(a)
    resultat= 2.71828 ** a
    return a


def factoriel(a):
    a=int(a)
    resultat=1
    for i in range(1,a+1):
        resultat *= i
    return resultat