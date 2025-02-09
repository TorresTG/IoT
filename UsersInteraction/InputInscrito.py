import os

from Inscrito import Inscrito

nombre_archivo = "CursoInput.json"
ruta_predeterCurs = "/Users/torres/Documents/pruebas_python/" + nombre_archivo

from Inscrito import VERDE, AMARILLO, ROJO, RESET


class InputCurso:

    def __init__(self, ciclo=True, superInscrito=Inscrito()):
        self.__ciclo = ciclo
        self.superInscrito = superInscrito
        self.inicializacion()

    def inicializacion(self):
        if os.path.exists(ruta_predeterCurs):
            print("añadiendo curso...")
            self.superInscrito.obtencion(ruta_predeterCurs, None, None, Inscrito)
            print(self.superInscrito)
        else:
            print("no se a encontrado ningun estudiante por el momento y se encuentra vacio a la espera de datos")
            self.superInscrito.crear_json(ruta_predeterCurs, [])


    @property
    def ciclo(self):
        return self.__ciclo

    def set_ciclo(self, value):
        self.__ciclo = value

    def recibir_inputs(self):
        d = {"nombre": str, "grado": str, "seccion": str, "salon": str, "descripcion": str}
        print("-------")
        for key in d.keys():
            print(f"introducir: {key}")
            d[key] = f"{input()}"
            print("-------")
        return d

    def verificacion(self):
        print("Introduzca el numero del curso(index) al cual ejecutar la accion: ")
        index = input()
        if index.isdigit():
            index = int(index)
            if index >= len(self.superInscrito.lista_clases) or index < 0:
                print("ese indice no existe crack")
                return False
            else:
                print(
                    f"¿Está seguro de realizar la accion deseada al siguiente dato?\n{self.superInscrito.lista_clases[index]}")
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

    def agregar_Curso(self):
        datos = self.recibir_inputs()
        x = Inscrito(**datos)
        self.superInscrito.agregar_a_Lista(x)
        self.superInscrito.depositar_datos(ruta_predeterCurs)
        print("Se ha añadido el Curso")
        print("-------")
        print("")

    def editar_Curso(self):
        index = self.verificacion()
        if index is not False:
            datos = self.recibir_inputs()
            x = Inscrito(**datos)
            self.superInscrito.editar_a_Lista(index, x)
            self.superInscrito.depositar_datos(ruta_predeterCurs)
            print("Se ha actualizado el Curso")
            print("-------")
            print("")


    def eliminar_Curso(self):
        index = self.verificacion()
        if index is not False:
            self.superInscrito.eliminar_a_Lista(index)
            self.superInscrito.depositar_datos(ruta_predeterCurs)
            print("Se ha actualizado el Curso")
            print("-------")
            print("")

    def ver_Curso(self):
        print(self.superInscrito)

    def empezarLaMatanga(self):
        while self.ciclo is True:
            print(f"--------Gestion De Cursos--------")
            print(f"1). Acceder a Estudiantes")
            print(f"2). Acceder a Estudiantes")
            print(f"{VERDE}1). Agregar a Inscrito{RESET}")
            print(f"{ROJO}3). Eliminar Curso{RESET}")
            print(f"4). Ver Todas los Curso")
            print(f"5). Salir devuelta a Inscritos")
            print("")
            print("")
            print("eliga el numero deseado")
            eleccion = input()
            if eleccion.isdigit():
                eleccion = int(eleccion)
            if eleccion == 1:
                self.agregar_Curso()
            elif eleccion == 2:
                self.editar_Curso()
            elif eleccion == 3:
                self.eliminar_Curso()
            elif eleccion == 4:
                self.ver_Curso()
            elif eleccion == 5:
                self.set_ciclo(False)
            else:
                print("ingrese un numero dentro del rango de 1 - 5")
        print("se cerro el programa")


inputs2 = InputCurso()
inputs2.empezarLaMatanga()
