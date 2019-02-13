from flask import Flask
from flask_cors import CORS

from services.MateriaService import MateriaService

app = Flask(__name__)

# DEFINICION DE CORS
CORS(app)

materia_service = MateriaService()

'''
INICIO - Endpoints Materias
'''


@app.route("/materias", methods=["GET"])
def listar_materias():
    return materia_service.obtener_materias()


@app.route("/materias/<int:materia>", methods=["GET"])
def obtener_materia(materia):
    return materia_service.obtener_materia_por_id(materia)


'''
FIN - Endpoints Materias
'''

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
