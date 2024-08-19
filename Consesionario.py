class Auto:
   def __init__(self, marca, modelo, tipo, color, motor, transmision, combustible, año, kilometraje, precio_compra):
       self.ruedas = 4
       self.capacidad = 5
       self.marca = marca
       self.modelo = modelo
       self.tipo = tipo  # Nacional o Importado
       self.color = color
       self.motor = motor
       self.transmision = transmision
       self.combustible = combustible
       self.año = año
       self.kilometraje = kilometraje
       self.precio_compra = precio_compra
       self.precio_venta = self.calcular_precio_venta()
   def calcular_precio_venta(self):
       return self.precio_compra * 1.4
   def mostrar_informacion(self):
       detalles = [
           f"Marca: {self.marca}",
           f"Modelo: {self.modelo}",
           f"Tipo: {self.tipo}",
           f"Color: {self.color}",
           f"Motor: {self.motor}",
           f"Transmisión: {self.transmision}",
           f"Combustible: {self.combustible}",
           f"Año: {self.año}",
           f"Kilometraje: {self.kilometraje} km",
           f"Precio de compra: ${self.precio_compra:.2f}",
           f"Precio de venta: ${self.precio_venta:.2f}",
           f"Ruedas: {self.ruedas}",
           f"Capacidad: {self.capacidad} pasajeros"
       ]
       return detalles

class Concesionario:
   def __init__(self):
       self.autos = []  # Lista para almacenar los autos
   def registrar_auto(self):
       marca = input("Ingrese la marca del auto: ")
       modelo = input("Ingrese el modelo del auto: ")
       tipo = input("Ingrese el tipo de auto (Nacional/Importado): ")
       color = input("Ingrese el color del auto: ")
       motor = input("Ingrese el tipo de motor (Ej. V6, V8, etc.): ")
       transmision = input("Ingrese el tipo de transmisión (Manual/Automática): ")
       combustible = input("Ingrese el tipo de combustible (Gasolina/Diésel/Eléctrico): ")
       año = input("Ingrese el año del auto: ")
       kilometraje = float(input("Ingrese el kilometraje del auto: "))
       precio_compra = float(input("Ingrese el precio de compra del auto: "))
       auto = Auto(marca, modelo, tipo, color, motor, transmision, combustible, año, kilometraje, precio_compra)
       self.autos.append(auto)
       print(f"\nEl auto {marca} {modelo} ha sido registrado con éxito.\n")
   def mostrar_autos(self):
       if not self.autos:
           print("No hay autos registrados.\n")
       else:
           print("Autos registrados:\n")
           for auto in self.autos:
               for detalle in auto.mostrar_informacion():
                   print(detalle)
               print("")  # Espacio entre autos
   def buscar_por_modelo(self):
       modelo_buscar = input("Ingrese el modelo del auto a buscar: ")
       encontrados = [auto for auto in self.autos if auto.modelo.lower() == modelo_buscar.lower()]
       if not encontrados:
           print(f"No se encontraron autos del modelo '{modelo_buscar}'.\n")
       else:
           print(f"Autos encontrados del modelo '{modelo_buscar}':\n")
           for auto in encontrados:
               for detalle in auto.mostrar_informacion():
                   print(detalle)
               print("")  # Espacio entre autos

# Ejemplo de uso
concesionario = Concesionario()
while True:
   print("1. Registrar un auto")
   print("2. Mostrar todos los autos")
   print("3. Buscar autos por modelo")
   print("4. Salir")
   opcion = input("Seleccione una opción: ")
   if opcion == "1":
       concesionario.registrar_auto()
   elif opcion == "2":
       concesionario.mostrar_autos()
   elif opcion == "3":
       concesionario.buscar_por_modelo()
   elif opcion == "4":
       break
   else:
       print("Opción no válida. Por favor, seleccione nuevamente.\n")