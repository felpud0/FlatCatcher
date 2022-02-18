

class Flat:
    def __init__(self,id,url,titulo,descripcion,precio):
        self.id=id
        self.url = url
        self.titulo = titulo
        self.descripcion = descripcion
        self.precio=precio
        self.coordenadas = 0,0
    
    def pretty(self):
        return "Id: {}\nUrl: {}\nTitulo: {}\nDescripcion: {}".format(self.id,self.url,self.titulo,self.descripcion)