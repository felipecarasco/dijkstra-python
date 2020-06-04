from models import No
from dijkstra import Dijkstra

def main():
    i = No("I")
    a = No("A")
    b = No("B")
    c = No("C")
    d = No("D")
    e = No("E")
    f = No("F")
    t = No("T")

    i.Conectar(a, 6)
    i.Conectar(b, 2)    
    a.Conectar(c, 4)
    a.Conectar(e, 2)
    b.Conectar(a, 4)
    b.Conectar(c, 3)
    b.Conectar(d, 7)
    c.Conectar(e, 2)
    c.Conectar(d, 3) 
    d.Conectar(t, 2)
    e.Conectar(t, 4)
    e.Conectar(f, 7)
    f.Conectar(t, 3)

    algoritmo = Dijkstra()
    caminho_mais_curto = algoritmo.EncontrarCaminhoMaisCurto(i, t)  
    
    print(*InverterCaminho(caminho_mais_curto).items(), sep = "\n") 

def InverterCaminho(caminho):
    caminho_ordenado = {}
    for no in reversed(caminho.keys()): 
        caminho_ordenado[no] = caminho[no]
    return caminho_ordenado

if __name__ == "__main__":
    main()