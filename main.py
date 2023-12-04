import kalkil

def kalkilsenp():
    print("****************************************************")
    print("******************KALKIL SENP***********************")
    print("****************************************************")

    print("1------- Adisyon")
    print("2------- Soustraksyon")
    print("3------- Miltipliksyon")
    print("4------- Divizyon")

    while True:
        chwa = input("Chwazi yon operasyon: ")
        chwa = int(chwa)

        if 1 <= chwa <= 4:
            break
        else:
            print("Mete yon chwa valab ant 1 ak 4.")

    if chwa==1:
        kalkil.adisyone()
    elif chwa==2:
         kalkil.soustraction()
    elif chwa==3:
         kalkil.miltiplikasyon()
    elif chwa==4:
         kalkil.divizyon()




def kalkilSyantifik():
    print("****************************************************")
    print("******************KALKIL SYANTIFIK******************")
    print("****************************************************")

    print("1------- kalkil faktoryel")
    print("2------- kalkil rasinn kare")
    print("3------- kalkil eksponansyel")
    while True:
        chwa = input("Chwazi yon operasyon: ")
        chwa = int(chwa)

        if 1 <= chwa <= 3:
            break
        else:
            print("Mete yon chwa valab ant 1 ak 3")
    if chwa==1:
        kalkil.kalkilFaktoryel()
    elif chwa==2:
         kalkil.kalkileRasinn()
    elif chwa==3:
         kalkil.exponentiel()
    




def menu():
    print("****************************************************")
    print("******************---MENU---************************")
    print("****************************************************")

    print("1----- kalkilatris senp")
    print("2------- kalkilatris syantifik")

    
    while True:
        chwa=input("kisa ou vle ?")
        chwa=int(chwa)
        if chwa ==1 or chwa ==2:
          break
        else:
            print("ou fe yon move chwa tranpri eseye anko")

    if  chwa== 1:
            kalkilsenp()
    elif chwa==2:
            kalkilSyantifik()
   

        
  

menu()