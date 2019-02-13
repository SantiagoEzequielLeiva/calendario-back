from config import DatabaseConfig
import pymysql


class Database(object):
    def __init__(self):
        self.host = DatabaseConfig.HOST
        self.user = DatabaseConfig.USER
        self.password = DatabaseConfig.PASSWORD
        self.db = DatabaseConfig.DB

        self.connection = None

    def abrirConexion(self):
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            cursorclass=pymysql.cursors.DictCursor
        )

    def cerrarConexion(self):
        self.connection.close()

    def obtenerConexion(self):
        if self.conexionNulaOCerrada():
            self.abrirConexion()

        return self.connection

    def conexionNulaOCerrada(self):
        return self.connection is None or (self.connection is not None and not self.connection.open)
