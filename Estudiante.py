class Estudiante:
    def __init__(self, nombre, edad, telefono, email, estado):
        self.__nombre = nombre
        self.__edad = edad
        self.__telefono = telefono
        self.__email = email
        self.__estado = estado

    def __str__(self):
        return f"{self._nombre}\n{self.edad}\n{self.telefono}\n{self.email}\n{self._estado}"

    def mostrar(self):
        print(self.__nombre)
        print(self.__edad)
        print(self.__telefono)
        print(self.__email)
        print(self.__estado)

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
    estudiansin = Estudiante("pepo", 5, "871674998", "pepe123@gmail.com", "muerto")
    print(estudiansin)
    print("---")
    estudiansin.set_edad(126)
    print(estudiansin)