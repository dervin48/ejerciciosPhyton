class Cola:
    def __init__(self):
        self.__items = []

    def EstaVacia(self):
        return len(self.__items) == 0

    def Encolar(self, item):
        self.__items.append(item)

    def Desencolar(self):
        return self.__items.pop(0)

    def LeerPrimerElemento(self):
        return self.__items[0]

    def NumeroElementos(self):
        return len(self.__items)

    def MostrarCola(self):
        print("Cola:", self.__items, "<-- Primer Elemento")

def SimuladorCola():
    cola = Cola()
    while True:
        print("""*****************
        Simulador de Cola 
        ******************

        Menu 
        1) Encolar
        2) Desencolar
        3) Leer primer elemento
        4) Numero de elementos
        5) Esta Vacia
        6) Mostrar Cola
        7) Salir""")
        
        opc = input("Opcion: ")
        
        if opc == '1':
            item = input("Introduzca elemento a encolar: ")
            cola.Encolar(item)
            print("Elemento encolado:", item)
        elif opc == '2':
            if cola.EstaVacia():
                print("La cola esta vacia, no se puede desencolar ningun elemento")
            else:
                item = cola.Desencolar()
                print("Elemento desencolado:", item)
        elif opc == '3':
            if cola.EstaVacia():
                print("La cola esta vacia, no se puede leer ningun elemento")
            else:
                print("El primer elemento es", cola.LeerPrimerElemento())
        elif opc == '4':
            print("La cola tiene", cola.NumeroElementos(), "elementos")
        elif opc == '5':
            if cola.EstaVacia():
                print("La cola esta vacia")
            else:
                print("La cola no esta vacia")
        elif opc == '6':
            cola.MostrarCola()
        elif opc == '7':
            break

SimuladorCola()
