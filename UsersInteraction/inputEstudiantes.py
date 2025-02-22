import json
import os

from pymongo import MongoClient

from Estudiante import Estudiante

nombre_archivo = "EstudianteInput.json"
ruta_predeterEstu = "/Users/torres/Documents/pruebas_python/" + nombre_archivo

nombre_archivo = "updateEstudiante.json"
ruta_update = "/Users/torres/Documents/pruebas_python/" + nombre_archivo

from Inscrito import VERDE, AMARILLO, ROJO, RESET


class InputEstudiante:

    def __init__(self, superEstudiante=None):
        self.__ciclo = True
        self.claseEnviada = False
        self.seteo_conexion = False
        self.internet = True

        if superEstudiante is None:
            self.superEstudiante = Estudiante()
            if os.path.exists(ruta_predeterEstu):
                print("añadiendo Estudiante...")
                self.superEstudiante.lista_clases = self.superEstudiante.obtencion(ruta_predeterEstu, None, Estudiante, None)
            else:
                print("no se a encontrado ningun Estudiante por el momento y se encuentra vacio a la espera de datos")
                self.superEstudiante.crear_json(ruta_predeterEstu, [])
        else:
            print("obteniendo datos de la clase mandada")
            self.superEstudiante = superEstudiante
            self.claseEnviada = True
            # con esto se obtiene los datos del Estudiante insertado y los guarda sobreescribiendo lo que haya en el json

        if not self.claseEnviada:
            if not os.path.exists(ruta_update):
                print("creando archivo temporal...")
                self.superEstudiante.crear_json(ruta_update, [])
            self.coleccion = self.coneccion_db() #enviar datos de updatejson
            with open(ruta_update, 'r') as f:
                contenido_real = json.load(f)
            if len(contenido_real) > 0:
                print("Enviando datos pendientes...")
                pendientes = self.superEstudiante.obtencion(ruta_update, None, Estudiante, None)
                self.enviar_a_mongo(pendientes)
                self.seteo_conexion = True
        print(self.superEstudiante)

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

            if self.seteo_conexion is True:
                print("Enviando datos pendientes...")
                pendientes = self.superEstudiante.obtencion(ruta_update, None, Estudiante, None)
                self.enviar_a_mongo(pendientes)

            if not self.internet:
                return None
            else:
                return db["Estudiantes"]
        except Exception as e:
            print(f"Error coneccion_db: {str(e)}")
            return None

    def enviar_a_mongo(self, lista_inscripciones):
        if lista_inscripciones == []:
            return
        documentos = [estu.to_dict() for estu in lista_inscripciones]
        self.coleccion.insert_many(documentos)
        print(f"Enviado {len(documentos)} registros a MongoDB")

        with open(ruta_update, "w") as f:
            json.dump([], f)



    def recibir_inputs(self):
        d = {"nombre": str, "edad": str, "telefono": str, "email": str, "estado": str}
        print("-------")
        for key in d.keys():
            print(f"introducir: {key}")
            d[key] = f"{input()}"
            print("-------")
        return d

    def actualizar(self):
        self.coleccion = self.coneccion_db()
        if self.coleccion is not None:
            lista_inscripciones = self.superEstudiante.obtencion(ruta_update, None, Estudiante, None)
            if lista_inscripciones:
                self.enviar_a_mongo(lista_inscripciones)
                self.superEstudiante.depositar_datos(ruta_predeterEstu)
            else:
                print("No hay datos para actualizar")
        else:
            print("Falló la conexión a MongoDB. Guardando localmente...")
            self.superEstudiante.depositar_datos(ruta_predeterEstu)
            self.superEstudiante.depositar_datos(ruta_update)



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
        if not self.claseEnviada:
            self.coleccion = self.coneccion_db()
            if self.coleccion is not None:
                self.actualizar()
                self.coleccion.insert_one(x.to_dict())
                print("Enviado a MongoDB correctamente")
            else:
                print("Sin conexión. Guardando en temporal...")
                self.superEstudiante.depositar_uno(ruta_update)
            self.superEstudiante.depositar_datos(ruta_predeterEstu)
            print(self.superEstudiante)
        else:
            print("Aviso: Se ha omitido el guardado de la clase en la DB y el Local")
            print(self.superEstudiante)

    def editar_Estudiante(self):
        index = self.verificacion()
        if index is not False:
            datos = self.recibir_inputs()
            x = Estudiante(**datos)
            self.superEstudiante.editar_a_Lista(index, x)
            if not self.claseEnviada:
                self.actualizar()
            else:
                print("Aviso: Se ha omitido el guardado de la clase en la DB y el Local")
                print(self.superEstudiante)

    def eliminar_Estudiante(self):
        index = self.verificacion()
        if index is not False:
            self.superEstudiante.eliminar_a_Lista(index)
            if not self.claseEnviada:
                self.actualizar()
            else:
                print("Aviso: Se ha omitido el guardado de la clase en la DB y el Local")
                print(self.superEstudiante)

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
            print(f"6). quitar internet (solo para pruebas)")
            print("")
            print(self.internet)
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
            elif eleccion == 6:
                if self.internet:
                    self.internet = False
                    self.coleccion = self.coneccion_db()
                else:
                    self.internet = True

            else:
                print("ingrese un numero dentro del rango de 1 - 6")
        print("se cerro el programa")
        r = self.superEstudiante.lista_clases
        self.superEstudiante.lista_clases = []
        return r


if __name__ == "__main__":
    estudiante = Estudiante()

    x = Estudiante("Matias", 2,
                   "8716764502", "tobias@gmail.com", "Vivo")

    y = Estudiante("noa", 19,
                   "8716608698", "23170106@uttcampus.com", "Muerto")
    estudiante.agregar_a_Lista(x)
    estudiante.agregar_a_Lista(y)
    #inputs2 = InputEstudiante(estudiante)
    inputs2 = InputEstudiante()
    inputs2.empezarLaMatanga()