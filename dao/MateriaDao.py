import logging

from dao.Database import Database


class MateriaDao(object):

    @staticmethod
    def listar_materias():
        try:
            with Database.get_instance().obtener_conexion().cursor() as cursor:
                logging.info("Se han encontrado %d registros", cursor.execute("SELECT id, descripcion FROM materia"))
                return cursor.fetchall()

        finally:
            Database.get_instance().cerrar_conexion()

    @staticmethod
    def obtener_materia_por_id(id_materia):
        try:
            with Database.get_instance().obtener_conexion().cursor() as cursor:
                logging.info("Buscando materia con id = %d", id_materia)
                cursor.execute("SELECT id, descripcion FROM materia WHERE id = %s", (id_materia))
                resultado = cursor.fetchone()
                logging.info("Resultado obtenido: %s", resultado)
                return resultado

        finally:
            Database.get_instance().cerrar_conexion()
