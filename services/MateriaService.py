from flask import jsonify

from dao.MateriaDao import MateriaDao


class MateriaService(object):
    def __init__(self):
        self.materia_dao = MateriaDao()

    def obtener_materias(self):
        return jsonify({"materias": self.materia_dao.listar_materias()})

    def obtener_materia_por_id(self, id_materia):
        return jsonify(self.materia_dao.obtener_materia_por_id(id_materia))
