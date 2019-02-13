from dao.Database import Database


class MateriaDao(object):
    def __init__(self):
        self.db = Database()

    def listarMaterias(self):
        conexion = self.db.obtenerConexion()

        try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT id, descripcion FROM materia")
                resultado = cursor.fetchall()
                return resultado

        finally:
            self.db.cerrarConexion()
