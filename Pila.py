class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        return self.items == []

    def ver_pila(self):
        if self.es_vacia():
            print("La pila está vacía.")
        else:
            print("Contenido de la pila (de abajo hacia arriba):")
            for elem in self.items:
                print(f" - {elem}")

def menu():
    pila = Pila()
    while True:
        print("\n===== MENÚ DE PILA =====")
        print("1. Apilar (agregar un elemento)")
        print("2. Desapilar (quitar el último elemento)")
        print("3. Ver si la pila está vacía")
        print("4. Mostrar la pila")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            dato = input("Ingresa el elemento a apilar: ")
            pila.apilar(dato)
            print(f"Elemento '{dato}' agregado a la pila.")

        elif opcion == "2":
            try:
                elem = pila.desapilar()
                print(f"Se desapiló el elemento: {elem}")
            except ValueError as e:
                print(e)

        elif opcion == "3":
            if pila.es_vacia():
                print("La pila está vacía.")
            else:
                print("La pila NO está vacía.")

        elif opcion == "4":
            pila.ver_pila()

        elif opcion == "5":
            print("¡Saliendo del programa!")
            break

        else:
            print("Opción no válida, intenta de nuevo.")


if __name__ == "__main__":
    menu()

