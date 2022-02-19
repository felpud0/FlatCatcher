

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

    def __hash__(self):
        return hash(self.id)
    def __eq__(self,other):
        if isinstance(other, Flat):
            return self.id == other.id
        return False

    def __str__(self) -> str:
        return "[{}] {} Precio: {}".format(self.id,self.titulo,self.precio)