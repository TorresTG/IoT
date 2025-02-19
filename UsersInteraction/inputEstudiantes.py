import os

from Estudiante import Estudiante

nombre_archivo = "EstudianteInput.json"
ruta_predeterEstu = "/Users/torres/Documents/pruebas_python/" + nombre_archivo

from Inscrito import VERDE, AMARILLO, ROJO, RESET


class InputEstudiante:

    def __init__(self, superEstudiante=None):
        self.__ciclo = True
        self.claseEnviada = True
        if superEstudiante is None:
            self.superEstudiante = Estudiante()
            if os.path.exists(ruta_predeterEstu):
                print("añadiendo Estudiante...")
                self.superEstudiante.obtencion(ruta_predeterEstu, None, Estudiante, None)
            else:
                print("no se a encontrado ningun estudiante por el momento y se encuentra vacio a la espera de datos")
                self.superEstudiante.crear_json(ruta_predeterEstu, [])
        else:
            print("obteniendo datos de la clase mandada")
            self.superEstudiante = superEstudiante
            self.claseEnviada = False
            # con esto se obtiene los datos del Estudiante insertado y los guarda sobreescribiendo lo que haya en el json
        print(self.superEstudiante)

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

    def actualizar_json(self):
        self.superEstudiante.depositar_datos(ruta_predeterEstu)
        print("Se ha añadido el Estudiante")
        print("-------")
        print("")

    def verificacion(self):
        print(f"\nÍndice del Estudiante a modificar (0/{len(self.superEstudiante.lista_clases) - 1}): ")
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
        if self.claseEnviada:
            self.actualizar_json()

    def editar_Estudiante(self):
        index = self.verificacion()
        if index is not False:
            datos = self.recibir_inputs()
            x = Estudiante(**datos)
            self.superEstudiante.editar_a_Lista(index, x)
            if self.claseEnviada:
                self.actualizar_json()

    def eliminar_Estudiante(self):
        index = self.verificacion()
        if index is not False:
            self.superEstudiante.eliminar_a_Lista(index)
            if self.claseEnviada:
                self.actualizar_json()

    def ver_Estudiante(self):
        print(self.superEstudiante)

    def empezarLaMatanga(self):
        while self.ciclo is True:
            print(f"--------Gestion De Estudiantes--------")
            print(f"{VERDE}1). Agregar Estudiante{RESET}")
            print(f"{AMARILLO}2). Editar Estudiante{RESET}")
            print(f"{ROJO}3). Eliminar Estudiante{RESET}")
            print(f"4). Ver Todas los Estudiante")
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
        return self.superEstudiante.lista_clases

if __name__ == "__main__":
    estudiante = Estudiante()
    """
    x = Estudiante("Matias", 2,
                   "8716764502", "tobias@gmail.com", "Vivo")

    y = Estudiante("noa", 19,
                   "8716608698", "23170106@uttcampus.com", "Muerto")
    estudiante.agregar_a_Lista(x)
    estudiante.agregar_a_Lista(y)"""
    #inputs2 = InputEstudiante(estudiante)
    inputs2 = InputEstudiante()
    inputs2.empezarLaMatanga()