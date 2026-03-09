class tomaDeDatos:
    def __init__(self, nombre, edad, añoNacimiento, telefono , direccion ):
        self.nombre = nombre
        self.edad = edad
        self.añoNacimiento = añoNacimiento
        self.telefono = telefono
        self.direccion = direccion
  


    def guardareDiccionario(self):
        return {
            "nombre":self. nombre,
            "edad": self.edad,
            "añoNacimiento": self.añoNacimiento,
            "telefono": self.telefono,
            "direccion": self.direccion
        }
      


#inter

datos = []

quieresIngresar = input("¿Desea ingresar sus datos? (si/no): ")

while quieresIngresar.lower() == "si":
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        añoNacimiento = int(input("Ingrese su año de nacimiento: "))
        telefono = input("Ingrese su teléfono: ")
        direccion = input("Ingrese su dirección: ")

        persona = tomaDeDatos(nombre, edad, añoNacimiento, telefono, direccion)
        datos.append(persona.guardareDiccionario())

        quieresIngresar = input("¿Desea ingresar sus datos nuevamente? (si/no): ")
       



print("\n los datos ingresados son :")
for d in datos:
    print(f"Nombre: {d['nombre']}, Edad: {d['edad']}, Año de Nacimiento: {d['añoNacimiento']}, Teléfono: {d['telefono']}, Dirección: {d['direccion']}")
    print(f"{d}")