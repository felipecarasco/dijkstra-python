class No:   
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.arestas = []
    
    def Atribuir(self, aresta):
        self.arestas.append(aresta)

    def Conectar(self, other, connection_value):
        Aresta.Criar(connection_value, self, other)

    def Vizinhos(self):
        vizinhos = []
        for aresta in self.arestas:   
            vizinhos.append(InformacaoVizinhos(
                aresta.no2 if aresta.no1 == self else aresta.no1, 
                aresta.valor))        
        return vizinhos    
        

class InformacaoVizinhos:   
    def __init__(self, no, peso_ate_no):
        self.no = no
        self.peso_ate_no = peso_ate_no


class Aresta:  
    def __init__(self, valor, no1, no2):
        self.valor = valor
        self.no1 = no1
        no1.Atribuir(self)
        self.no2 = no2
        no2.Atribuir(self)        
    
    def Criar(valor, no1, no2):
        return Aresta(valor, no1, no2)