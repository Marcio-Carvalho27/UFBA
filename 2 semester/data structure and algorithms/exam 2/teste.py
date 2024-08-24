class Elemento:
    def __init__(self, n):
        self.anterior = None
        self.proximo = None
        self.no = n

class Fila:
    def __init__(self):
        self.final = None
        self.inicio = None
        self.tamanhoFila = 0

    def desenfileirar(self):
        if self.inicio is not None:
            self.tamanhoFila -= 1
            aux = self.inicio
            self.inicio = aux.proximo
            return aux.no

    def enfileirar(self, n):
        self.tamanhoFila += 1
        if self.inicio is None:
            self.inicio = n
        else:
            n.anterior = self.final
            self.final.proximo = n
        self.final = n

    def imprimirFila(self, i):
        k = 1
        for j in range(1, self.tamanhoFila+1):
            if 2**k == j:
                k += 1
                print()
            print(f'{i.no.valorHeap} ', end='')
            if i.proximo is not None:
                i = i.proximo
        print()

class NoHeap:
    def __init__(self, valor):
        self.direita = None
        self.esquerda = None
        self.pai = None
        self.posicao = 1
        self.valorHeap = valor

class HeapMin:
    def __init__(self):
        self.raiz = None
        self.tamanhoHeap = 0
        self.ultimo = None

    def inserir(self, n):
        self.tamanhoHeap += 1
        if self.raiz is None:
            self.raiz = n
            self.ultimo = n
            n.posicao = self.tamanhoHeap
        else:
            self.inserirSubarvore(self.raiz, n)

    def inserirSubarvore(self, r, n):
        f0 = Fila()
        f0.enfileirar(Elemento(r))
        while f0.inicio is not None:
            aux = f0.desenfileirar()
            if aux.esquerda is not None:
                f0.enfileirar(Elemento(aux.esquerda))
                if aux.direita is not None:
                    f0.enfileirar(Elemento(aux.direita))
                else:
                    aux.direita = n
                    n.pai = aux
                    n.posicao = self.tamanhoHeap
                    self.ultimo = n
                    self.fixUp(aux.direita)
                    f0.final = None
                    f0.inicio = None
            else:
                aux.esquerda = n
                n.pai = aux
                n.posicao = self.tamanhoHeap
                self.ultimo = n
                self.fixUp(aux.esquerda)
                f0.final = None
                f0.inicio = None

    def fixUp(self, n):
        if n.pai is not None:
            if n.pai.valorHeap >= n.valorHeap:
                aux = n.valorHeap
                n.valorHeap = n.pai.valorHeap
                n.pai.valorHeap = aux
                self.fixUp(n.pai)
        else:
            self.raiz = n

    def remover(self, r):
        aux = self.ultimo
        if self.tamanhoHeap > 1:
            if aux.pai.direita == aux:    
                aux.pai.direita = None
            else:
                aux.pai.esquerda = None
            if r.direita is not None:
                aux.direita = r.direita
                r.direita.pai = aux
            if r.esquerda is not None:
                aux.esquerda = r.esquerda
                r.esquerda.pai = aux
            aux.pai = None
            aux.posicao = 1
            self.raiz = aux
            self.fixDown(self.raiz)
            self.tamanhoHeap -= 1
            self.procurarUltimo(self.tamanhoHeap, self.raiz)
        elif self.tamanhoHeap == 1:
            self.raiz = None
            self.tamanhoHeap -= 1
            self.ultimo = None
        return r.valorHeap

    def fixDown(self, r):
        if r.esquerda is not None and r.direita is not None:
            if r.esquerda.valorHeap < r.direita.valorHeap:
                if r.esquerda.valorHeap < r.valorHeap:
                    aux = r.valorHeap
                    r.valorHeap = r.esquerda.valorHeap
                    r.esquerda.valorHeap = aux
                    self.fixDown(r.esquerda)
            else:
                if r.direita.valorHeap < r.valorHeap:
                    aux = r.valorHeap
                    r.valorHeap = r.direita.valorHeap
                    r.direita.valorHeap = aux
                    self.fixDown(r.direita)
        elif r.esquerda is not None and r.direita is None:
            if r.esquerda.valorHeap < r.valorHeap:
                aux = r.valorHeap
                r.valorHeap = r.esquerda.valorHeap
                r.esquerda.valorHeap = aux
                self.fixDown(r.esquerda)

    def procurarUltimo(self, n, r):
        if r is not None:
            if r.posicao == n:
                self.ultimo = r
            else:
                self.procurarUltimo(n, r.direita)
                self.procurarUltimo(n, r.esquerda)

    def heapFila(self, f1, r):
        f0 = Fila()
        f0.enfileirar(Elemento(r))
        while f0.inicio is not None:
            aux = f0.desenfileirar()
            f1.enfileirar(Elemento(aux))
            if aux.esquerda is not None:
                f0.enfileirar(Elemento(aux.esquerda))
                if aux.direita is not None:
                    f0.enfileirar(Elemento(aux.direita))
        return f1

    def max(self, f1, i):
        if f1.tamanhoFila > 1:
            while i.proximo.no.esquerda is not None:
                i = i.proximo
            while i is not None:
                self.fixDownMax(i.no)
                i = i.anterior

    def fixDownMax(self, n):
        if n.esquerda is not None and n.direita is not None:
            if n.esquerda.valorHeap > n.direita.valorHeap:
                if n.esquerda.valorHeap > n.valorHeap:
                    aux = n.valorHeap
                    n.valorHeap = n.esquerda.valorHeap
                    n.esquerda.valorHeap = aux
                    self.fixDownMax(n.esquerda)
            else:
                if n.direita.valorHeap > n.valorHeap:
                    aux = n.valorHeap
                    n.valorHeap = n.direita.valorHeap
                    n.direita.valorHeap = aux
                    self.fixDownMax(n.direita)
        elif n.esquerda is not None and n.direita is None:
            if n.esquerda.valorHeap > n.valorHeap:
                aux = n.valorHeap
                n.valorHeap = n.esquerda.valorHeap
                n.esquerda.valorHeap = aux
                self.fixDownMax(n.esquerda)

def main():
    N = input()
    N = int(N)
    F0 = Fila()
    F1 = Fila()
    H = HeapMin()
    for i in range(0, N):
        C, I = (input().split())
        I = int(I)
        if C == 'I':
            H.inserir(NoHeap(I))
        else:
            for i in range(0, I):
                print(f'{H.remover(H.raiz)} ', end='')
            if I != 0:
                print()
    if H.tamanhoHeap > 0:
        H.heapFila(F0, H.raiz)
        H.max(F0, F0.inicio)
        H.heapFila(F1, H.raiz)
        F1.imprimirFila(F1.inicio)

main()
