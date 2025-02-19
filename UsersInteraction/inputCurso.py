import os

from Curso import Curso

nombre_archivo = "CursoInput.json"
ruta_predeterCurs = "/Users/torres/Documents/pruebas_python/" + nombre_archivo

from Inscrito import VERDE, AMARILLO, ROJO, RESET


class InputCurso:

    def __init__(self, superCurso=None):
        self.__ciclo = True
        self.claseEnviada = True #se activa el guardado del json
        if superCurso is None:
            self.superCurso = Curso()
            if os.path.exists(ruta_predeterCurs):
                print("añadiendo curso...")
                self.superCurso.obtencion(ruta_predeterCurs, Curso, None, None)
            else:
                print("no se a encontrado ningun estudiante por el momento y se encuentra vacio a la espera de datos")
                self.superCurso.crear_json(ruta_predeterCurs, [])
        else:
            print("obteniendo datos de la clase mandada")
            self.superCurso = superCurso
            self.claseEnviada = False # se desactiva el gurdado del json
            # con esto se obtiene los datos del curso insertado y los guarda sobreescribiendo lo que haya en el json
        print(self.superCurso)

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

    def actualizar_json(self):
        self.superCurso.depositar_datos(ruta_predeterCurs)
        print("Curso a recibido cambios")
        print("-------")
        print("")

    def verificacion(self):
        print(f"\nÍndice del Curso a modificar (0/{len(self.superCurso.lista_clases) - 1}): ")
        index = input()
        if index.isdigit():
            index = int(index)
            if index >= len(self.superCurso.lista_clases) or index < 0:
                print("ese indice no existe crack")
                return False
            else:
                print(
                    f"¿Está seguro de realizar la accion deseada al siguiente dato?\n{self.superCurso.lista_clases[index]}")
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
        x = Curso(**datos)
        self.superCurso.agregar_a_Lista(x)
        if self.claseEnviada: #checa si se envio la clase en el constructor si acierta, guarda en el json
            self.actualizar_json()

    def editar_Curso(self):
        index = self.verificacion()
        if index is not False:
            datos = self.recibir_inputs()
            x = Curso(**datos)
            self.superCurso.editar_a_Lista(index, x)
            if self.claseEnviada:
                self.actualizar_json()

    def eliminar_Curso(self):
        index = self.verificacion()
        if index is not False:
            self.superCurso.eliminar_a_Lista(index)
            if self.claseEnviada:
                self.actualizar_json()

    def ver_Curso(self):
        print(self.superCurso)

    def empezarLaMatanga(self):
        while self.ciclo is True:
            print(f"--------Gestion De Cursos--------")
            print(f"{VERDE}1). Agregar Curso{RESET}")
            print(f"{AMARILLO}2). Editar Curso{RESET}")
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
        return self.superCurso

if __name__ == "__main__":

    ClaseCurso = Curso()

    x = Curso("matematicas", 5,
              "A", "salon 17", "se ensenan formulas basicas")

    y = Curso("geologia", 6,
              "B", "salon 22", "se miran las gemas")

    z = Curso("espanol", 3,
              "A", "salon 4", "se estudia el lenguaje")
    ClaseCurso.agregar_a_Lista(x)
    ClaseCurso.agregar_a_Lista(y)
    ClaseCurso.agregar_a_Lista(z)

    #inputs1 = InputCurso(ClaseCurso)
    inputs1 = InputCurso()
    inputs1.empezarLaMatanga()
