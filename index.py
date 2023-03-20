
#Ejercicio 6

class Persona:
    def __init__(self, nombre = "Nombre", edad = 0, dni= 0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if type(nombre) == str: 
            self.__nombre = nombre
        else: print("Ingresó un dato incorrecto.")


    @property
    def edad(self):
        self.__edad

    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int):
            self.__edad = edad
        else: print("Ingresó un dato incorrecto.")

    @property
    def dni(self):
        self.__dni

    @dni.setter
    def dni(self, dni):
        if isinstance(dni, int):
            self.__dni = dni
        else: print("Ingresó un dato incorrecto.")

    def mostrar(self):
        print (f"Apellido y Nombre: {self.__nombre}. Edad: {self.__edad}. DNI: {self.__dni}")

    def es_mayor_de_edad():
        if edad>=18:
            return True
        else: return False


usuario = Persona("Juan Perez", 35, 35008965)
usuario.mostrar()


#Ejercicio 7

class Cuenta:
    def __init__(self, nombre = Persona(), cantidad = 0):
        self.__titular = nombre
        self.__cantidad = cantidad

    
    @property
    def titular(self):
        return self.__titular

    @titular.setter   
    def titular(self, nombre):
        self.__titular = nombre

    @property
    def cantidad(self):
        self.__cantidad

    @cantidad.setter   
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        print (f"Apellido y Nombre: {self.__titular}. Saldo en la cuenta: {self.__cantidad}")

    def ingresar(self,cantidad):
        if cantidad > 0:
            self.__cantidad = self.__cantidad + cantidad
        
    def retirar(self, cantidad):
        self.__cantidad = self.__cantidad - cantidad



usuario2 = Cuenta("Juliana Ortiz", 500)
usuario2.ingresar(45000)
usuario2.retirar(5000)
usuario2.mostrar()




