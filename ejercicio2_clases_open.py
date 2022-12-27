
class Alumno:

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def datos(self):
        print(f"Nombre: {self.nombre}\n"
              f"Nota: {self.nota}")

        if self.nota > 0 and self.nota < 3.5:
            print("No Aprobado\n")
        else:
            print("Aprobado\n")


alumno1 = Alumno("Juan", 3.5)
alumno1.datos()

alumno2 = Alumno("Andrea", 4.5)
alumno2.datos()

alumno3 = Alumno("Javier", 2)
alumno3.datos()
