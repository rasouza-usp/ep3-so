# algoritmos de substituicao de paginas

class Page:
    def __init__ (self, inicio, p):
        self.tamanho = p                 #define o tamanho da pagina
        self.inicio = int(inicio)        #onde a pagina comeca
        self.fim = int(inicio) + p - 1   #onde a pagina termina
        self.mapeada = 0                 #mapeada = 1 se a pagina esta mapeada na memoria fisica e 0 cc


def optimal():
    print 'optimal'

def fin_fout():
    print 'First-In, First-Out'

def LRUv2():
    print 'Least Recentely Used (Segunda versao)'

def LRUv4():
    print 'Least Recentely Used (Quarta versao)'
