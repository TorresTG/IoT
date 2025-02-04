import json

from Methods import Methods
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
RESET = "\033[0m"





class Estudiante(Methods):
    def __init__(self, nombre = None, edad = None, telefono = None, email = None, estado = None):
        if (nombre or edad or telefono or email or estado) is None:
            super().__init__()
        else:
            self.__nombre = nombre
            self.__edad = edad
            self.__telefono = telefono
            self.__email = email
            self.__estado = estado

    def __str__(self):
        datos = {
            key.replace(f"_{self.__class__.__name__}__", ""): value
            for key, value in self.__dict__.items()
        }
        return json.dumps(datos, indent=4, ensure_ascii=False)


    @property
    def nombre(self):
        return self.__nombre

    @property
    def telefono(self):
        return self.__telefono

    def set_nombre(self, value):
        self.__nombre = value

    def set_edad(self, value):
        self.__edad = value

    def set_telefono(self, value):
        self.__telefono = value

    def set_email(self, value):
        self.__email = value

    def set_estado(self, value):
        self.__estado = value


if __name__ == "__main__":
    ClaseEstudiante = Estudiante()
    x = Estudiante("Matias", 2,
              "8716764502", "tobias@gmail.com", "Vivo")

    y = Estudiante("noa", 19,
              "8716608698", "23170106@uttcampus.com", "Muerto")

    print(f"{VERDE}----POST AGREGAR ESTUDIANTE----{RESET}")
    ClaseEstudiante.agregar_a_Lista(x)
    ClaseEstudiante.agregar_a_Lista(y)
    ClaseEstudiante.mostrar_Lista()
    print("")

    print(f"{ROJO}----POST ELIMINAR ESTUDIANTE----{RESET}")
    ClaseEstudiante.eliminar_a_Lista(1)
    ClaseEstudiante.mostrar_Lista()
    print("")

    print(f"{AMARILLO}----POST EDITAR ESTUDIANTE----{RESET}")
    a = Estudiante("Eduardo", -5,
              "8716764502", "eduardo@gmail.com", "Muelto")

    ClaseEstudiante.editar_a_Lista(0, a)
    ClaseEstudiante.mostrar_Lista()