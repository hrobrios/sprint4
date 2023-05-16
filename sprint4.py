import json

class Usuario:
    def __init__(self, nombre, edad, nivel):
        self.nombre = nombre
        self.edad = edad
        self.nivel=nivel

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo nivel {self.nivel}")

    def to_dict(self):
        return {
            'nombre': self.nombre,
            'edad': self.edad
        }

class UsuarioPremium(Usuario):
    def __init__(self, nombre, edad, nivel):
        super().__init__(nombre, edad, nivel)#se utiliza para acceder a los métodos de la clase base desde la subclase
        self.nivel = nivel

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo un nivel  {self.nivel}.")

    def to_dict(self):
        data = super().to_dict()#llamo al método de la clase para obtener diccionario conlos atributos
        data['nivel'] = self.nivel#creo variable con ese diccionario 
        return data

class ManejoErrores:
    def validar_edad(self, edad):#metodo para verificar si edad es mayor o igual a 18 y muestra excepcion si edad no cumple requisito
        try:
            if int(edad) < 18:
                raise ValueError("La edad debe ser mayor o igual a 18.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            return True

    def guardar_json(self, usuarios, archivo):
        try:#manejo de excepciones
            with open(archivo, 'w') as file:#archivo se cerrará tras el uso
                json.dump(usuarios, file, indent=6)#funcion para escribir diccionario en archivo json, con 4 espacios de sangr+ia
        except IOError as e:#
            print(f"Error al guardar el archivo: {e}")

class ManejoExcepciones:
    def leer_json(self, archivo):
        try:
            with open(archivo, 'r') as file:#apertura y letura arhcivo con cierre de este.
                data = json.load(file)#variable data muestra info de archivo
                return data
        except FileNotFoundError:
            print(f"El archivo {archivo} no existe.")
        except json.JSONDecodeError as e:
            print(f"Error al leer el archivo JSON: {e}")


usuario1 = Usuario("Juan", 25, "ahí nomás")
usuario2 = UsuarioPremium("María", 30, "Gold")

usuarios = [usuario1.to_dict(), usuario2.to_dict()]

manejo_errores = ManejoErrores()
manejo_errores.guardar_json(usuarios, "usuarios.json")

manejo_excepciones = ManejoExcepciones()
datos = manejo_excepciones.leer_json("usuarios.json")
print(datos)
usuario1.saludar(), usuario2.saludar()

