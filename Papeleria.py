class Producto:
   def __init__(self, categoria, especificacion, costo_base):
       self.categoria = categoria
       self.especificacion = especificacion
       self.costo_base = costo_base
       self.marca = self.definir_marca()
       self.precio_final = self.calcular_precio_final()
   def definir_marca(self):
       if self.categoria == "cuaderno":
           return "HOJITAS"
       elif self.categoria == "lapiz":
           return "RAYAS"
       else:
           return "Desconocida"
   def calcular_precio_final(self):
       return self.costo_base * 1.30
   def obtener_informacion(self):
       detalles = [
           f"Categoría: {self.categoria.capitalize()}",
           f"Especificación: {self.especificacion}",
           f"Marca: {self.marca}",
           f"Costo Base: ${self.costo_base:.2f}",
           f"Precio Final: ${self.precio_final:.2f}"
       ]
       return detalles

class Tienda:
   def __init__(self):
       self.inventario = []  # Lista para almacenar los productos
   def registrar_producto(self):
       categoria = input("Ingrese la categoría del producto (cuaderno/lapiz): ").lower()
       if categoria == "cuaderno":
           especificacion = input("Ingrese la cantidad de hojas (50/100): ")
           if especificacion not in ["50", "100"]:
               print("Cantidad de hojas no válida. Debe ser 50 o 100.")
               return
       elif categoria == "lapiz":
           especificacion = input("Ingrese el tipo de lápiz (grafito/colores): ").lower()
           if especificacion not in ["grafito", "colores"]:
               print("Tipo de lápiz no válido. Debe ser grafito o colores.")
               return
       else:
           print("Categoría de producto no válida.")
           return
       costo_base = float(input("Ingrese el costo base del producto: "))
       producto = Producto(categoria, especificacion, costo_base)
       self.inventario.append(producto)
       print(f"\nEl producto {categoria} ha sido registrado con éxito.\n")
   def mostrar_inventario(self):
       if not self.inventario:
           print("No hay productos registrados.\n")
       else:
           print("Productos registrados:\n")
           for producto in self.inventario:
               for detalle in producto.obtener_informacion():
                   print(detalle)
               print("")  # Espacio entre productos

# Ejemplo de uso
tienda = Tienda()
while True:
   print("1. Registrar un producto")
   print("2. Mostrar todos los productos")
   print("3. Salir")
   opcion = input("Seleccione una opción: ")
   if opcion == "1":
       tienda.registrar_producto()
   elif opcion == "2":
       tienda.mostrar_inventario()
   elif opcion == "3":
       break
   else:
       print("Opción no válida. Por favor, seleccione nuevamente.\n")