from flask import jsonify

from dao.MateriaDao import MateriaDao


class MateriaService(object):
    @staticmethod
    def obtener_materias():
        return jsonify({"materias": MateriaDao.listar_materias()})

    @staticmethod
    def obtener_materia_por_id(id_materia):
        return jsonify(MateriaDao.obtener_materia_por_id(id_materia))
