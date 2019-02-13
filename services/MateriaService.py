from flask import jsonify

from model.Materia import Materia
from dao.MateriaDao import MateriaDao

class MateriaService(object):

    def obtenerMaterias():
        return jsonify({"materias": MateriaDao().listarMaterias()})
