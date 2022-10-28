class vehiculo:
    def __init__(self,color,ruedas,puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    def __str__(self):
        return "color {}, {} ruedas, {} puertas".format(self.color,self.ruedas,self.puertas)

class coche(vehiculo):
    def __init__(self, color, ruedas, puertas,velocidad,cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return super().__str__()+", {} Km/h, {} cm^3".format(self.velocidad,self.cilindrada)

c = coche("rojo",4,5,220,1600)
print(c)