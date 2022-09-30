class Vehiculo():
    color = 'Negro'
    ruedas = 4
    puertas = 5

class Coche(Vehiculo):
    velocidad = 180
    cilindrara = 2000

mazda = Coche()
mazda.color = 'Blanco'

print(f'Color: {mazda.color}')
print(f'Ruedas: {mazda.ruedas}')
print(f'Puertas: {mazda.puertas}')
print(f'Velocidad: {mazda.velocidad}')
print(f'Cilindrada: {mazda.cilindrara}')