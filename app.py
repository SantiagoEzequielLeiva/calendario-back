import logging

from flask import Flask
from flask_cors import CORS

from services.MateriaService import MateriaService

app = Flask(__name__)

# DEFINICION DE CORS
CORS(app)

'''
INICIO - Endpoints Materias
'''


@app.route("/materias", methods=["GET"])
def listar_materias():
    logging.info("INICIO GET - /materias")
    response = MateriaService.obtener_materias()
    logging.info("FIN GET - /materias")
    return response


@app.route("/materias/<int:materia>", methods=["GET"])
def obtener_materia(materia):
    logging.info("INICIO GET - /materias/%d", materia)
    response = MateriaService.obtener_materia_por_id(materia)
    logging.info("FIN GET - /materias/%d", materia)
    return response


'''
FIN - Endpoints Materias
'''

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s [%(levelname)s] --- %(module)s: %(message)s', level=logging.INFO)
    app.run(host='0.0.0.0', port=5000, debug=True)
