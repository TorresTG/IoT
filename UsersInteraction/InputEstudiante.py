import os

from Inscrito import Inscrito
from Estudiante import Estudiante

nombre_archivo = "EstudianteInput.json"
ruta_predeterEstu = "/Users/torres/Documents/pruebas_python/" + nombre_archivo

from Inscrito import VERDE, AMARILLO, ROJO, RESET


class InputEstudiante:

    def __init__(self, ciclo=True, superEstudiante=Estudiante()):
        self.__ciclo = ciclo
        self.superEstudiante = superEstudiante
        self.inicializacion()

    def inicializacion(self):
        if os.path.exists(ruta_predeterEstu):
            print("añadiendo estudiantes...")
            self.superEstudiante.obtencion(ruta_predeterEstu, None, Estudiante, None)
            print(self.superEstudiante)
        else:
            print("no se a encontrado ningun estudiante por el momento y se encuentra vacio a la espera de datos")

    @property
    def ciclo(self):
        return self.__ciclo

    def set_ciclo(self, value):
        self.__ciclo = value

    def recibir_inputs(self):
        d = {"nombre": str, "edad": str, "telefono": str, "email": str, "estado": str}
        print("-------")
        for key in d.keys():
            print(f"introducir: {key}")
            d[key] = f"{input()}"
            print("-------")
        return d

    def verificacion(self):
        print("Introduzca el numero del estudiante(index) al cual ejecutar la accion: ")
        index = input()
        if index.isdigit():
            index = int(index)
            if index >= len(self.superEstudiante.lista_clases) or index < 0:
                print("ese indice no existe crack")
                return False
            else:
                print(
                    f"¿Está seguro de realizar la accion deseada al siguiente dato?\n{self.superEstudiante.lista_clases[index]}")
                print(f"\n Desea continuar? (y/n):")
                confirmacion = input()
                if confirmacion == "y":
                    return index
                elif confirmacion == "n":
                    print("Se cancelo la edicion")
                    return False
                else:
                    print("por favor, ingrese una letra valida")
                    return False
        else:
            print("ingrese un numero valido")
            return False

    def agregar_Estudiante(self):
        datos = self.recibir_inputs()
        x = Estudiante(**datos)
        self.superEstudiante.agregar_a_Lista(x)
        self.superEstudiante.depositar_datos(ruta_predeterEstu)
        print("Se ha añadido el estudiante")
        print("-------")
        print("")

    def editar_Estudiante(self):
        index = self.verificacion()
        if index is not False:
            datos = self.recibir_inputs()
            x = Estudiante(**datos)
            self.superEstudiante.editar_a_Lista(index, x)
            self.superEstudiante.depositar_datos(ruta_predeterEstu)
            print("Se ha atualizado el estudiante")
            print("-------")
            print("")


    def eliminar_Estudiante(self):
        index = self.verificacion()
        if index is not False:
            self.superEstudiante.eliminar_a_Lista(index)
            self.superEstudiante.depositar_datos(ruta_predeterEstu)
            print("Se ha atualizado el estudiante")
            print("-------")
            print("")

    def ver_Estudiante(self):
        print(self.superEstudiante)

    def empezarLaMatanga(self):
        while self.ciclo is True:
            print(f"--------Gestion De Estudiante--------")
            print(f"{VERDE}1). Agregar Estudiante{RESET}")
            print(f"{AMARILLO}2). Editar Estudiante{RESET}")
            print(f"{ROJO}3). Eliminar Estudiante{RESET}")
            print(f"4). Ver Todas los Estudiantes")
            print(f"5). Salir devuelta a Inscritos")
            print("")
            print("")
            print("eliga el numero deseado")
            eleccion = input()
            if eleccion.isdigit():
                eleccion = int(eleccion)
            if eleccion == 1:
                self.agregar_Estudiante()
            elif eleccion == 2:
                self.editar_Estudiante()
            elif eleccion == 3:
                self.eliminar_Estudiante()
            elif eleccion == 4:
                self.ver_Estudiante()
            elif eleccion == 5:
                self.set_ciclo(False)
            else:
                print("ingrese un numero dentro del rango de 1 - 5")
        print("se cerro el programa")


inputs1 = InputEstudiante()
inputs1.empezarLaMatanga()
