anyo = input("[i] Por favor, introduzca a continuación el año que desea comprobar si es bisiesto o no: > ")

modulo4 = int(anyo) % 4
modulo100 = int(anyo) % 100
modulo400 = int(anyo) % 400

def comprobacion():
    bisiesto = False
    if modulo4 == 0 and modulo100 !=0 :
        bisiesto = True
    elif modulo100 == 0 and modulo400 != 0:
        bisiesto = False
    elif modulo400 == 0:
        bisiesto = True
    else:
        bisiesto = False
    if bisiesto == False :
        print("[i] El año que ha introducido no es bisiesto.")
    elif bisiesto == True:
        print("[i] El año que ha introducido es bisiesto.")

comprobacion()