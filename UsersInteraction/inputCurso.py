import json
import os

from pymongo import MongoClient

from Curso import Curso

nombre_archivo = "CursoInput.json"
ruta_predeterCurs = "/Users/torres/Documents/pruebas_python/" + nombre_archivo

nombre_archivo = "updateCurso.json"
ruta_update = "/Users/torres/Documents/pruebas_python/" + nombre_archivo

from Inscrito import VERDE, AMARILLO, ROJO, RESET


class InputCurso:

    def __init__(self, superCurso=None):
        self.__ciclo = True
        self.claseEnviada = False #se activa el guardado del json
        self.seteo_conexion = False
        self.internet = True

        if superCurso is None:
            self.superCurso = Curso()
            if os.path.exists(ruta_predeterCurs):
                print("añadiendo Curso...")
                self.superCurso.lista_clases = self.superCurso.obtencion(ruta_predeterCurs, Curso, None, None)
            else:
                print("no se a encontrado ningun Curso por el momento y se encuentra vacio a la espera de datos")
                self.superCurso.crear_json(ruta_predeterCurs, [])
        else:
            print("obteniendo datos de la clase mandada")
            self.superCurso = superCurso
            self.claseEnviada = False # se desactiva el gurdado del json
            # con esto se obtiene los datos del curso insertado y los guarda sobreescribiendo lo que haya en el json

        if not self.claseEnviada:
            if not os.path.exists(ruta_update):
                print("creando archivo temporal...")
                self.superCurso.crear_json(ruta_update, [])
            self.coleccion = self.coneccion_db()  # enviar datos de updatejson
            if os.path.getsize(ruta_update) > 0:
                print("Enviando datos pendientes...")
                pendientes = self.superCurso.obtencion(ruta_update, Curso, None, None)
                self.enviar_a_mongo(pendientes)
                self.seteo_conexion = True
        print(self.superCurso)

    @property
    def ciclo(self):
        return self.__ciclo

    def set_ciclo(self, value):
        self.__ciclo = value

    def coneccion_db(self):
        try:
            MONGO_URI = "mongodb+srv://Mac-Tobi:04477369@myatlasclusteredu.qenui.mongodb.net/?authSource=admin"
            client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
            db = client["python"]
            print("Conexión exitosa a MongoDB")

            # Enviar datos pendientes si existen
            if os.path.getsize(ruta_update) > 0 and self.seteo_conexion is True:
                print("Enviando datos pendientes...")
                pendientes = self.superCurso.obtencion(ruta_update, Curso, None, None)
                self.enviar_a_mongo(pendientes)
            if self.internet == False:
                return None
            else:
                return db["Cursos"]
        except Exception as e:
            print(f"Error coneccion_db: {str(e)}")
            return None

    def enviar_a_mongo(self, lista_inscripciones):
        if lista_inscripciones == []:
            return
        documentos = [cur.to_dict() for cur in lista_inscripciones]
        self.coleccion.insert_many(documentos)
        print(f"Enviado {len(documentos)} registros a MongoDB")

        with open(ruta_update, "w") as f:
            json.dump([], f)

    def recibir_inputs(self):
        d = {"nombre": str, "grado": str, "seccion": str, "salon": str, "descripcion": str}
        print("-------")
        for key in d.keys():
            print(f"introducir: {key}")
            d[key] = f"{input()}"
            print("-------")
        return d

    def actualizar(self):
        self.coleccion = self.coneccion_db()
        if self.coleccion is not None:
            lista_inscripciones = self.superCurso.obtencion(ruta_update, Curso, None, None)
            if lista_inscripciones:
                self.enviar_a_mongo(lista_inscripciones)
                self.superCurso.depositar_datos(ruta_predeterCurs)
            else:
                print("No hay datos para actualizar")
        else:
            print("Falló la conexión a MongoDB. Guardando localmente...")
            self.superCurso.depositar_datos(ruta_predeterCurs)
            self.superCurso.depositar_datos(ruta_update)


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
        if not self.claseEnviada:
            self.coleccion = self.coneccion_db()
            if self.coleccion is not None:
                self.actualizar()
                self.coleccion.insert_one(x.to_dict())
                print("Enviado a MongoDB correctamente")
            else:
                print("Sin conexión. Guardando en temporal...")
                self.superCurso.depositar_uno(ruta_update)
            self.superCurso.depositar_datos(ruta_predeterCurs)
            print(self.superCurso)
        else:
            print("Aviso: Se ha omitido el guardado de la clase en la DB y el Local")
            print(self.superCurso)

    def editar_Curso(self):
        index = self.verificacion()
        if index is not False:
            datos = self.recibir_inputs()
            x = Curso(**datos)
            self.superCurso.editar_a_Lista(index, x)
            if not self.claseEnviada:
                self.actualizar()
            else:
                print("Aviso: Se ha omitido el guardado de la clase en la DB y el Local")
                print(self.superCurso)

    def eliminar_Curso(self):
        index = self.verificacion()
        if index is not False:
            self.superCurso.eliminar_a_Lista(index)
            if not self.claseEnviada:
                self.actualizar()
            else:
                print("Aviso: Se ha omitido el guardado de la clase en la DB y el Local")
                print(self.superCurso)

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
            print(f"6). quitar internet (solo para pruebas)")
            print("")
            print(self.internet)
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
            elif eleccion == 6:
                if self.internet:
                    self.internet = False
                else:
                    self.internet = True
                    self.coleccion = self.coneccion_db()
            else:
                print("ingrese un numero dentro del rango de 1 - 6")
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
