
class Alumno:
# programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota.
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
# Deberéis de definir los métodos para inicializar sus atributos,
# imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
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
