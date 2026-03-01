class tomaDeDatos:
    def __init__(self, nombre, edad, añoNacimiento, telefono , direccion ):
        self.nombre = nombre
        self.edad = edad
        self.añoNacimiento = añoNacimiento
        self.telefono = telefono
        self.direccion = direccion
  
        
        
    def guardareDcionario(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "añoNacimiento": self.añoNacimiento,
            "telefono": self.telefono,
            "direccion":     self.direccion
        }                
        
    def pila(self):
        pila = []
        pila.append(self.guardareDicionario())
        return pila
 


    def mostrarDatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Año de Nacimiento: {self.añoNacimiento}")
        print(f"Teléfono: {self.telefono}")
        print(f"Dirección: {self.direccion}")
"""        
tados = tomaDeDatos("Juan Pérez", 30, 1994, "555-1234", "Calle Falsa 123")
tados.mostrarDatos()    
toma1 = tomaDeDatos("María Gómez", 25, 1999, "555-5678", "Avenida Siempre Viva 456")
toma1.mostrarDatos()
toma2 = tomaDeDatos("Pedro Martínez", 40, 1983, "555-8765", "Boulevard de los Sueños 789")
toma2.mostrarDatos()
""" 

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
añoNacimiento = int(input("Ingrese su año de nacimiento: "))
telefono = input("Ingrese su teléfono: ")
direccion = input("Ingrese su dirección: ")

def main(nombre, edad, añoNacimiento, telefono, direccion):
    tomaInput = tomaDeDatos(nombre, edad, añoNacimiento, telefono, direccion)
    tomaInput.mostrarDatos()

#inter 
quieresIngresar = input("¿Desea ingresar sus datos? (si/no): ")
while quieresIngresar.lower() == "si":
    main(nombre, edad, añoNacimiento, telefono, direccion)
    quieresIngresar = input("¿Desea ingresar sus datos nuevamente? (si/no): ")
    
#main(nombre, edad, añoNacimiento, telefono, direccion)
#outpush
#print(main(nombre, edad, añoNacimiento, telefono, direccion))
