from dao.Database import Database


class MateriaDao(object):
    def __init__(self):
        self.db = Database()

    def listar_materias(self):
        try:
            with self.db.obtener_conexion().cursor() as cursor:
                cursor.execute("SELECT id, descripcion FROM materia")
                resultado = cursor.fetchall()
                return resultado

        finally:
            self.db.cerrar_conexion()

    def obtener_materia_por_id(self, id_materia):
        try:
            with self.db.obtener_conexion().cursor() as cursor:
                cursor.execute("SELECT id, descripcion FROM materia WHERE id = %s", (id_materia))
                resultado = cursor.fetchone()
                return resultado

        finally:
            self.db.cerrar_conexion()
