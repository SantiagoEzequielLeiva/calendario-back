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
def listarMaterias():
    return MateriaService.obtenerMaterias()


'''
FIN - Endpoints Materias
'''

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )
