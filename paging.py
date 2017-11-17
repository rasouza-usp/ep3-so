# algoritmos de substituicao de paginas

#classe page: representa uma pagina na tabela de paginas
class Page:
    def __init__ (self, inicio, p):
        self.tamanho = p                 #define o tamanho da pagina
        self.inicio = int(inicio)        #onde a pagina comeca
        self.fim = int(inicio) + p - 1   #onde a pagina termina
        self.presente = 0                #presente = 1 se a pagina esta mapeada na memoria fisica e 0 caso contrario
        self.link = -1                   #link recebe o indice da pagina que esta linkada na memoria fisica
        self.procId = -1                 #O id do processo dono desta pagina
        


def optimal():
    print 'optimal'

def fin_fout():
    print 'First-In, First-Out'

def LRUv2():
    print 'Least Recentely Used (Segunda versao)'

def LRUv4():
    print 'Least Recentely Used (Quarta versao)'
