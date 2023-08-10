class Nodo():
    def __init__(self,id, dato):
        self.id = id
        self.dato = dato
        self.siguiente = None

    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id

    def getDato(self):
        return self.dato
    
    def setDato(self, dato):
        self.dato = dato

    def getSiguiente(self):
        return self.siguiente
    
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente