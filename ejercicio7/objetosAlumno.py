class alumno:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    def get_datos(self):
        print("Nombre: "+self.nombre)
        print("Nota: "+str(self.nota))
    def is_aprobado(self):
        if self.nota < 5:
            print("El alumno "+self.nombre+" no ha aprobado")
        else:
            print("El alumno "+self.nombre+" ha aprobado")

a = alumno("Pepe",4)
b = alumno("Paco",6)
a.get_datos()
a.is_aprobado()
b.get_datos()
b.is_aprobado()