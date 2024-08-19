class Libro:
   def __init__(self, titulo, autor, isbn):
       self.titulo = titulo
       self.autor = autor
       self.isbn = isbn
       self.estado = "Disponible"  # Estado inicial
   def prestar(self):
       if self.estado == "Disponible":
           self.estado = "Prestado"
           return True
       return False
   def devolver(self):
       if self.estado == "Prestado":
           self.estado = "Disponible"
           return True
       return False
   def mostrar_info(self):
       return (f"Título: {self.titulo}\n"
               f"Autor: {self.autor}\n"
               f"ISBN: {self.isbn}\n"
               f"Estado: {self.estado}")

class Biblioteca:
   def __init__(self):
       self.libros = []
   def agregar_libro(self):
       titulo = input("Ingrese el título del libro: ")
       autor = input("Ingrese el autor del libro: ")
       isbn = input("Ingrese el ISBN del libro: ")
       libro = Libro(titulo, autor, isbn)
       self.libros.append(libro)
       print(f"\nEl libro '{titulo}' ha sido agregado con éxito.\n")
   def prestar_libro(self):
       isbn = input("Ingrese el ISBN del libro a prestar: ")
       for libro in self.libros:
           if libro.isbn == isbn:
               if libro.prestar():
                   print(f"\nEl libro '{libro.titulo}' ha sido prestado.\n")
               else:
                   print("El libro no está disponible para prestar.\n")
               return
       print("Libro no encontrado.\n")
   def devolver_libro(self):
       isbn = input("Ingrese el ISBN del libro a devolver: ")
       for libro in self.libros:
           if libro.isbn == isbn:
               if libro.devolver():
                   print(f"\nEl libro '{libro.titulo}' ha sido devuelto.\n")
               else:
                   print("El libro no está prestado.\n")
               return
       print("Libro no encontrado.\n")
   def mostrar_libros(self):
       if not self.libros:
           print("No hay libros en la biblioteca.\n")
       else:
           print("Libros en la biblioteca:\n")
           for libro in self.libros:
               print(libro.mostrar_info())
               print("")  # Espacio entre libros

# Ejemplo de uso
biblioteca = Biblioteca()
while True:
   print("1. Agregar un libro")
   print("2. Prestar un libro")
   print("3. Devolver un libro")
   print("4. Mostrar todos los libros")
   print("5. Salir")
   opcion = input("Seleccione una opción: ")
   if opcion == "1":
       biblioteca.agregar_libro()
   elif opcion == "2":
       biblioteca.prestar_libro()
   elif opcion == "3":
       biblioteca.devolver_libro()
   elif opcion == "4":
       biblioteca.mostrar_libros()
   elif opcion == "5":
       break
   else:
       print("Opción no válida. Por favor, seleccione nuevamente.\n")