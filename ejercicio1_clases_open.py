# ? Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
"""
-Velocidad
-Cilindrada
"""


class Vehiculo:
    color = None
    ruedas = 0
    puertas = 0

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


# * En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
"""
-Color
-Ruedas
-Puertas
"""


class Coche(Vehiculo):
    def __init__(self, velocidad, cilindraje, color, ruedas, puertas):
        super().__init__(color, ruedas, puertas)

        self.velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        datos = f'El coche tiene las siguientes caracateristicas: \nColor: {self.color}\nRuedas: {self.ruedas}\nPuertas: {self.puertas}\nVelocidad: {self.velocidad}\nCilindraje: {self.cilindraje}'
        return datos


auto = Coche(12, 582, 'Azul', 2, 4)
# ! Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.
print(auto)
