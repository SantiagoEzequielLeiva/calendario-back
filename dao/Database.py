from config import DatabaseConfig
import pymysql


class Database(object):
    def __init__(self):
        self.host = DatabaseConfig.HOST
        self.user = DatabaseConfig.USER
        self.password = DatabaseConfig.PASSWORD
        self.db = DatabaseConfig.DB

        self.connection = None

    def abrir_conexion(self):
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            db=self.db,
            cursorclass=pymysql.cursors.DictCursor
        )

    def cerrar_conexion(self):
        self.connection.close()

    def obtener_conexion(self):
        if self.conexion_nula_o_cerrada():
            self.abrir_conexion()

        return self.connection

    def conexion_nula_o_cerrada(self):
        return self.connection is None or (self.connection is not None and not self.connection.open)
