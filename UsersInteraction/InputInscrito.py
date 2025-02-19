import os

from Inscrito import Inscrito, VERDE, AMARILLO, ROJO, RESET
from Curso import Curso
from Estudiante import Estudiante
from UsersInteraction.inputEstudiantes import InputEstudiante

nombre_archivo = "InscritoInput.json"
ruta_predeterInsc = "/Users/torres/Documents/pruebas_python/" + nombre_archivo

class InputInscrito:

    def __init__(self, superInscrito=None):
        self.__ciclo = True
        self.claseEnviada = True
        if superInscrito is None:
            self.superInscrito = Inscrito()
            if os.path.exists(ruta_predeterInsc):
                print("añadiendo Inscritos...")
                self.superInscrito.obtencion(ruta_predeterInsc, Curso, Estudiante, Inscrito)
            else:
                print("no se a encontrado ningun inscrito por el momento y se encuentra vacio a la espera de datos")
                self.superInscrito.crear_json(ruta_predeterInsc, [])# arreglar esto
        else:
            print("obteniendo datos de la clase mandada")
            self.superInscrito = superInscrito
            self.claseEnviada = False
            # con esto se obtiene los datos del Inscrito insertado y los guarda sobreescribiendo lo que haya en el json
        print(self.superInscrito)

    @property
    def ciclo(self):
        return self.__ciclo

    def set_ciclo(self, value):
        self.__ciclo = value

    def recibir_inputs(self):
        d = {"curso": Curso, "estudiantes": Estudiante}  # Inicialmente asignas las clases
        p = {"nombre": str, "grado": str, "seccion": str, "salon": str, "descripcion": str}
        print("-------")
        for key in p.keys():
            print(f"introducir: {key}")
            p[key] = input()
            print("-------")
        d["curso"] = Curso(**p)
        inter = InputEstudiante(estudiante)
        d["estudiantes"] = inter.empezarLaMatanga()
        return d

    def agregar(self):
        datos = self.recibir_inputs()
        x = Inscrito(datos["curso"])
        for estu in datos["estudiantes"]:
            x.estudiantes.agregar_a_Lista(estu)
        self.superInscrito.agregar_a_Lista(x)
        if self.claseEnviada:
            self.actualizar_json()


    def actualizar_json(self):
        self.superInscrito.depositar_datos(ruta_predeterInsc)
        print("Se ha añadido el Inscrito")
        print("-------")
        print("")

    def verificacion(self):
        print(f"\nÍndice del Inscrito a modificar (0/{len(self.superInscrito.lista_clases) - 1}): ")
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



    def editar(self):
        index = self.verificacion()
        if index is not False:
            datos = self.recibir_inputs()
            x = Inscrito(datos["cursos"])
            for estu in datos["estudiantes"]:
                x.estudiantes.agregar_a_Lista(estu)
            self.superInscrito.editar_a_Lista(index, x)
            if self.claseEnviada:
                self.actualizar_json()

    def eliminar(self):
        index = self.verificacion()
        if index is not False:
            self.superInscrito.eliminar_a_Lista(index)
            if self.claseEnviada:
                self.actualizar_json()

    def ver(self):
        print(self.superInscrito)

    def empezarLaMatanga(self):
        while self.ciclo is True:
            print(f"--------Gestion De Inscrito--------")
            print(f"{VERDE}1). Agregar Inscrito{RESET}")
            print(f"{AMARILLO}2). Editar Inscrito{RESET}")
            print(f"{ROJO}3). Eliminar Inscrito{RESET}")
            print(f"4). Ver Todas los Inscrito")
            print(f"5). Salir de Inscritos")
            print("")
            print("")
            print("eliga el numero deseado")
            eleccion = input()
            if eleccion.isdigit():
                eleccion = int(eleccion)
            if eleccion == 1:
                self.agregar()
            elif eleccion == 2:
                self.editar()
            elif eleccion == 3:
                self.eliminar()
            elif eleccion == 4:
                self.ver()
            elif eleccion == 5:
                self.set_ciclo(False)
            else:
                print("ingrese un numero dentro del rango de 1 - 5")
        print("se cerro el programa")

if __name__ == "__main__":
    estudiante = Inscrito()

    """x = Curso("matematicas", 5, "A", "salon 17", "se ensenan formulas basicas")
    xa = Estudiante("pepo", 5, "871674998", "pepe123@gmail.com", "muerto")

    inscripcion1 = Inscrito(x)
    inscripcion1.estudiantes.agregar_a_Lista(xa)"""
    #inputs2 = InputEstudiante(estudiante)
    inputs2 = InputInscrito()
    inputs2.empezarLaMatanga()