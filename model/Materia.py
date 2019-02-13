class Materia(object):
    def __init__(self, id, descripcion):
        self.id = id
        self.descripcion = descripcion

    def comoJson(self):
        return {"id": self.id, "descripcion": self.descripcion}
