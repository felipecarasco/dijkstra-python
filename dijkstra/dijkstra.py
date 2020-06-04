import sys
from models import Aresta
from models import No
from models import InformacaoVizinhos


class Peso:
    def __init__(self, origem, valor):
        self.origem = origem
        self.valor = valor


class Visita:
    def __init__(self):
        self.visitados = []
        self.pesos = {}
        self.pendentes_visita = []

    def RegistrarVisita(self, no):
        if no not in self.visitados:
            self.visitados.append(no)
    
    def FoiVisitado(self, no):
        return no in self.visitados

    def AtualizarPeso(self, no, novo_peso):
        self.pesos[no] = novo_peso
    
    def BuscarPeso(self, no):
        if no not in self.pesos:
            peso = Peso(None, int(sys.maxsize/2))
        else:
            peso = self.pesos[no]
        return peso
    
    def BuscarValorPeso(self, no):
        return self.BuscarPeso(no).valor

    def PendenteVisita(self, no):
        self.pendentes_visita.append(no)

    def ExisteVisitaPendente(self):
        return len(self.pendentes_visita) > 0

    def ObterNoParaVisita(self):
        visita_pendente_ordenada = sorted(self.pendentes_visita, key=self.BuscarValorPeso)        
        no = visita_pendente_ordenada[0]
        self.pendentes_visita.remove(no)
        return no
    
    def PossuiCaminhoEstimadoAteOrigem(self, no):
        return self.BuscarPeso(no).origem is not None

    def EstimarCaminhoAteOrigem(self, no):        
        caminho = {}
        while no is not None:   
            caminho[no.etiqueta] = self.BuscarValorPeso(no)
            no = self.BuscarPeso(no).origem        
        return caminho


class Dijkstra:
    def EncontrarCaminhoMaisCurto(self, origem, para):    
        visita = Visita()

        visita.AtualizarPeso(origem, Peso(None, 0))
        visita.PendenteVisita(origem)

        while visita.ExisteVisitaPendente():   
            no_visitado = visita.ObterNoParaVisita()
            peso_no_visitado = visita.BuscarPeso(no_visitado)
            visita.RegistrarVisita(no_visitado)
           
            for informacao_vizinhos in no_visitado.Vizinhos():           
                if visita.FoiVisitado(informacao_vizinhos.no) != True:
                    visita.PendenteVisita(informacao_vizinhos.no)
                
                peso_vizinho = visita.BuscarPeso(informacao_vizinhos.no)

                peso_provavel = (peso_no_visitado.valor + informacao_vizinhos.peso_ate_no)
                if peso_vizinho.valor > peso_provavel:
                    visita.AtualizarPeso(informacao_vizinhos.no, Peso(no_visitado, peso_provavel))        
       
        return visita.EstimarCaminhoAteOrigem(para) if visita.PossuiCaminhoEstimadoAteOrigem(para) else None