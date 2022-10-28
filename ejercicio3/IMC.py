peso = input("[?] Por favor, introduzca su peso en Kg: > ")
altura = input("[?] Por favor, introduzca su altura en m: > ")
# imc = peso/estatura^2
imc = float(peso)/(float(altura)*float(altura))
print("[i] Su IMC es: "+"%.2f" %imc)