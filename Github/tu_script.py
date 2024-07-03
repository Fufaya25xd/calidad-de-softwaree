# Funciones para agregar, mostrar, buscar y eliminar datos...

# Función para agregar un dato a la lista
def agregar_dato(lista):
    dato = input("Ingrese el dato a agregar: ")
    lista.append(dato)
    print(f"Dato '{dato}' agregado a la lista.")

# Función para mostrar todos los datos de la lista
def mostrar_datos(lista):
    if lista:
        print("Datos en la lista:")
        for dato in lista:
            print(dato)
    else:
        print("La lista está vacía.")

# Función para buscar un dato en la lista
def buscar_dato(lista):
    dato = input("Ingrese el dato a buscar: ")
    if dato in lista:
        print(f"Dato '{dato}' encontrado en la lista.")
    else:
        print(f"Dato '{dato}' no encontrado en la lista.")

# Función para eliminar un dato de la lista
def eliminar_dato(lista):
    dato = input("Ingrese el dato a eliminar: ")
    if dato in lista:
        lista.remove(dato)
        print(f"Dato '{dato}' eliminado de la lista.")
    else:
        print(f"Dato '{dato}' no encontrado en la lista.")

# Programa principal
def main():
    lista = []
    while True:
        print("\nSeleccione una opción:")
        print("1. Agregar dato")
        print("2. Mostrar datos")
        print("3. Buscar dato")
        print("4. Eliminar dato")
        print("5. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == '1':
            agregar_dato(lista)
        elif opcion == '2':
            mostrar_datos(lista)
        elif opcion == '3':
            buscar_dato(lista)
        elif opcion == '4':
            eliminar_dato(lista)
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar el programa principal si se ejecuta este archivo directamente
if __name__ == "__main__":
    main()
