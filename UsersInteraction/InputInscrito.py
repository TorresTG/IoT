import json
import os

from Inscrito import Inscrito, VERDE, AMARILLO, ROJO, RESET
from Curso import Curso
from Estudiante import Estudiante
from UsersInteraction.inputEstudiantes import InputEstudiante

from pymongo import MongoClient


nombre_archivo = "InscritoInput.json"
ruta_predeterInsc = "/Users/torres/Documents/pruebas_python/" + nombre_archivo
nombre_archivo = "updateInscrito.json"
ruta_update = "/Users/torres/Documents/pruebas_python/" + nombre_archivo

class InputInscrito:

    def __init__(self, superInscrito=None):
        self.__ciclo = True
        self.claseEnviada = True
        self.superInscrito = Inscrito()
        if superInscrito is None:
            if os.path.exists(ruta_predeterInsc):
                print("Cargando inscripciones principales...")
                self.superInscrito.lista_clases = self.superInscrito.obtencion(ruta_predeterInsc, Curso, Estudiante, Inscrito)
            else:
                self.superInscrito.crear_json(ruta_predeterInsc, [])
        else:
            self.superInscrito = superInscrito
        self.coleccion = self.coneccion_db()  # Intenta conectar y envía datos pendientes

        # Preparar archivo temporal si no existe
        if not os.path.exists(ruta_update):
            self.superInscrito.crear_json(ruta_update, [])
        print(self.superInscrito)

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
            if os.path.getsize(ruta_update) > 0:
                print("Enviando datos pendientes...")
                pendientes = self.superInscrito.obtencion(ruta_update, Curso, Estudiante, Inscrito)
                self.enviar_a_mongo(pendientes)

            return db["Inscritos"]
        except Exception as e:
            print(f"Error de conexión: {str(e)}")
            return None

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

    def enviar_a_mongo(self, lista_inscripciones):
        if not lista_inscripciones:
            return
        try:
            documentos = [insc.to_dict() for insc in lista_inscripciones]
            self.coleccion.insert_many(documentos)
            print(f"Enviados {len(documentos)} registros a MongoDB")

            # Limpiar archivo temporal
            with open(ruta_update, "w") as f:
                json.dump([], f)
        except Exception as e:
            print(f"Error crítico al enviar: {str(e)}")

    #arreglar con Conexion
    def actualizar(self):
        self.coleccion = self.coneccion_db()
        if self.coleccion is not None:
            # Cargar datos desde el archivo updateInscrito.json
            lista_inscripciones = self.superInscrito.obtencion(ruta_update, Curso, Estudiante, Inscrito)

            if lista_inscripciones:
                self.enviar_a_mongo(lista_inscripciones)
                self.superInscrito.depositar_datos(ruta_predeterInsc)
            else:
                print("No hay datos para actualizar")
        else:
            print("Falló la conexión a MongoDB. Guardando localmente...")
            self.superInscrito.depositar_datos(ruta_predeterInsc)
            self.superInscrito.depositar_datos(ruta_update)


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

    def agregar(self):
        datos = self.recibir_inputs()
        nueva_inscripcion = Inscrito(datos["curso"])

        # Agregar estudiantes
        for estu in datos["estudiantes"]:
            nueva_inscripcion.estudiantes.agregar_a_Lista(estu)

        # Guardar en JSON principal siempre
        self.superInscrito.agregar_a_Lista(nueva_inscripcion)
        self.superInscrito.depositar_datos(ruta_predeterInsc)
        print(self.superInscrito)
        # Manejo de conexión
        if self.coleccion != []:
            try:
                self.coleccion.insert_one(nueva_inscripcion.to_dict())
                print("Enviado a MongoDB inmediatamente")
            except Exception as e:
                print(f"Error al enviar: {str(e)}. Guardando en temporal...")
                self.superInscrito.depositar_uno(ruta_update)
        else:
            print("Sin conexión. Guardando en temporal...")
            self.superInscrito.depositar_uno(ruta_update)

    def editar(self):
        index = self.verificacion()
        if index is not False:
            datos = self.recibir_inputs()
            x = Inscrito(datos["cursos"])
            for estu in datos["estudiantes"]:
                x.estudiantes.agregar_a_Lista(estu)
            self.superInscrito.editar_a_Lista(index, x)
            if self.claseEnviada:
                self.actualizar()

    def eliminar(self):
        index = self.verificacion()
        if index is not False:
            self.superInscrito.eliminar_a_Lista(index)

            self.actualizar()

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

    x = Curso("matematicas", 5, "A", "salon 17", "se ensenan formulas basicas")
    xa = Estudiante("pepo", 5, "871674998", "pepe123@gmail.com", "muerto")

    inscripcion1 = Inscrito(x)
    inscripcion1.estudiantes.agregar_a_Lista(xa)
    #inputs2 = InputEstudiante(inscripcion1)
    inputs2 = InputInscrito()
    inputs2.empezarLaMatanga()