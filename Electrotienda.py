class Dispositivo:
   def __init__(self, tipo, marca, modelo, color, memoria, procesador, precio_compra):
       self.tipo = tipo         # Celular, Tablet, o Portátil
       self.marca = marca       # En este caso, siempre será PHR
       self.modelo = modelo
       self.color = color
       self.memoria = memoria   # Memoria RAM o almacenamiento
       self.procesador = procesador
       self.precio_compra = precio_compra
       self.precio_venta = self.calcular_precio_venta()
   def calcular_precio_venta(self):
       return self.precio_compra * 1.7
   def mostrar_informacion(self):
       detalles = [
           f"Tipo: {self.tipo}",
           f"Marca: {self.marca}",
           f"Modelo: {self.modelo}",
           f"Color: {self.color}",
           f"Memoria: {self.memoria}",
           f"Procesador: {self.procesador}",
           f"Precio de compra: ${self.precio_compra:.2f}",
           f"Precio de venta: ${self.precio_venta:.2f}"
       ]
       return detalles

class Almacen:
   def __init__(self):
       self.dispositivos = []  # Lista para almacenar los dispositivos
   def registrar_dispositivo(self):
       tipo = input("Ingrese el tipo de dispositivo (Celular/Tablet/Portátil): ")
       marca = "PHR"  # Marca fija para todos los dispositivos
       modelo = input("Ingrese el modelo del dispositivo: ")
       color = input("Ingrese el color del dispositivo: ")
       memoria = input("Ingrese la memoria del dispositivo (Ej. 4GB RAM, 128GB almacenamiento): ")
       procesador = input("Ingrese el procesador del dispositivo: ")
       precio_compra = float(input("Ingrese el precio de compra del dispositivo: "))
       dispositivo = Dispositivo(tipo, marca, modelo, color, memoria, procesador, precio_compra)
       self.dispositivos.append(dispositivo)
       print(f"\nEl dispositivo {modelo} ha sido registrado con éxito.\n")
   def mostrar_dispositivos(self):
       if not self.dispositivos:
           print("No hay dispositivos registrados.\n")
       else:
           print("Dispositivos registrados:\n")
           for dispositivo in self.dispositivos:
               for detalle in dispositivo.mostrar_informacion():
                   print(detalle)
               print("")  # Espacio entre dispositivos
   def buscar_por_tipo(self):
       tipo_buscar = input("Ingrese el tipo de dispositivo a buscar (Celular/Tablet/Portátil): ")
       encontrados = [dispositivo for dispositivo in self.dispositivos if dispositivo.tipo.lower() == tipo_buscar.lower()]
       if not encontrados:
           print(f"No se encontraron dispositivos del tipo '{tipo_buscar}'.\n")
       else:
           print(f"Dispositivos encontrados del tipo '{tipo_buscar}':\n")
           for dispositivo in encontrados:
               for detalle in dispositivo.mostrar_informacion():
                   print(detalle)
               print("")  # Espacio entre dispositivos

# Ejemplo de uso
almacen = Almacen()
while True:
   print("1. Registrar un dispositivo")
   print("2. Mostrar todos los dispositivos")
   print("3. Buscar dispositivos por tipo")
   print("4. Salir")
   opcion = input("Seleccione una opción: ")
   if opcion == "1":
       almacen.registrar_dispositivo()
   elif opcion == "2":
       almacen.mostrar_dispositivos()
   elif opcion == "3":
       almacen.buscar_por_tipo()
   elif opcion == "4":
       break
   else:
       print("Opción no válida. Por favor, seleccione nuevamente.\n")