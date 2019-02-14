import logging

from dao.Database import Database


class MateriaDao(object):
    def __init__(self):
        self.db = Database()

    def listar_materias(self):
        try:
            with self.db.obtener_conexion().cursor() as cursor:
                logging.info("Se han encontrado %d registros", cursor.execute("SELECT id, descripcion FROM materia"))
                return cursor.fetchall()

        finally:
            self.db.cerrar_conexion()

    def obtener_materia_por_id(self, id_materia):
        try:
            with self.db.obtener_conexion().cursor() as cursor:
                logging.info("Buscando materia con id = %d", id_materia)
                cursor.execute("SELECT id, descripcion FROM materia WHERE id = %s", (id_materia))
                resultado = cursor.fetchone()
                logging.info("Resultado obtenido: %s", resultado)
                return resultado

        finally:
            self.db.cerrar_conexion()
