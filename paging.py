from memory import *

# algoritmo de substituicao de paginas

global matriz_LRUv2

#classe page: representa uma pagina na tabela de paginas
class Page:
    def __init__ (self, inicio, p):
        self.tamanho = p                 #define o tamanho da pagina
        self.inicio = int(inicio)        #onde a pagina comeca
        self.fim = int(inicio) + p - 1   #onde a pagina termina
        self.presente = 0                #presente = 1 se a pagina esta mapeada na memoria fisica e 0 caso contrario
        self.mapeada = -1                #link recebe o indice da pagina que esta linkada na memoria fisica
        self.procId = -1                 #O id do processo dono desta pagina
        self.tAcesso = -1
        self.m = 0
        self.r = 0

    def show(self):
        print 'Pg: [' + str(self.inicio) + '->'+str(self.fim)+']; pid: ' + str(self.procId)
        
    # retorna o valor do bit presente/ausente    
    def get_presente(self):
        return self.presente
        
    # altera o bit presente/ausente    
    def set_presente(self,bit):
        self.presente = bit
        
    # retorna o pid do processo que usa essa pagina    
    def get_procId(self):
        return self.procId
        
    # altera o pid do processo que usa essa pagina    
    def set_procId(self,pid):
        self.procId = pid
        
    # retorna o indice da pag que foi mapeada da mem fisica pra virtual    
    def get_mapeada(self):
        return self.mapeada
        
    # altera o indice da pag que foi mapeada da mem fisica pra virtual
    def set_mapeada(self,indice):
        self.mapeada = indice
        
    # retorna o valor do bit m    
    def get_m(self):
        return self.m
        
    # altera o valor do bit m    
    def set_m(self,indice):
        self.m = indice

    # retorna o valor do bit r    
    def get_r(self):
        return self.r
        
    # altera o valor do bit r    
    def set_r(self,indice):
        self.r = indice
        
    # retorna o valor do tempo de acesso    
    def get_tAcesso(self):
        return self.tAcesso
        
    # altera o valor do tempo de acesso
    def set_tAcesso(self,indice):
        self.tAcesso = indice
        
        
        
def optimal():
    print 'optimal'

# First In First Out
def fin_fout(mem_virtual,mem_fisica,indiceVirtual,clock,procId):

    remover = 0
    #verifica qual eh a pagina mais velha alocada
    
    #pego o tempo da primeira pagina da tabela de paginas para comecar
    old = mem_fisica.tabela[0].get_tAcesso()
    i = 0
    for pagina in mem_fisica.tabela:
        if pagina.get_tAcesso() < old:
            old = pagina.get_tAcesso()
            remover = i
        i += 1
    
    #faz o bit presente da pagina que vai deixar de ser mapeada = 0
    virt = mem_fisica.tabela[remover].get_mapeada()
    mem_virtual.tabela[virt].set_presente(0)
    
    #mapeia a nova pagina
    mapeia_virtual_to_fisica(mem_virtual,mem_fisica,indiceVirtual,remover, clock, procId)

def LRUv2 (mem_virtual,mem_fisica,indiceVirtual,clock,procId):
    global matriz_LRUv2
    npaginas = len(matriz_LRUv2)
    
    # define pagina a ser removida
    remover = LRUv2_pagina (npaginas)
    
    #faz o bit presente da pagina que vai deixar de ser mapeada = 0
    virt = mem_fisica.tabela[remover].get_mapeada()
    mem_virtual.tabela[virt].set_presente(0)
    
    # marca o acesso na matriz_LRUv2 da nova pagina acessada que entrou no lugar da pagina removida
    matriz_LRUv2 = marca_matriz (remover,npaginas, matriz_LRUv2)
    
    #mapeia a nova pagina
    mapeia_virtual_to_fisica(mem_virtual,mem_fisica,indiceVirtual,remover, clock, procId)

# inicia matriz de tamanho npaginas X npaginas
def matriz_LRUv2_init(npaginas):
    global matriz_LRUv2
    matriz_LRUv2 = [["0" for i in range(npaginas)] for j in range(npaginas)]
    return matriz_LRUv2

def marca_linha(linha,npaginas,matriz):
    for j in range(npaginas):
        matriz[linha][j] = '1'
    return matriz

def marca_coluna(coluna,npaginas,matriz):
    for i in range(npaginas):
        matriz[i][coluna] = '0'
    return matriz

def marca_matriz (pagina,npaginas,matriz):
    matriz = marca_linha(pagina,npaginas,matriz)
    matriz = marca_coluna(pagina,npaginas,matriz)
    return matriz

# devolve a pagina menos acessada de acordo com a matriz de acesso matriz_LRUv2
def LRUv2_pagina (npaginas):
    global matriz_LRUv2
    maior = int(''.join(npaginas*['1']),2)
    pagina = 0
    for i in range(npaginas):
        x = int(''.join(matriz_LRUv2[i]),2)
        if x < maior:
            pagina = i 
            maior = x
    return pagina

def LRUv4():
    print 'Least Recentely Used (Quarta versao)'

#Recebe as memorias virtual e fisica e mapeia as paginas de acordo com os indices 
def mapeia_virtual_to_fisica(mem_virtual,mem_fisica,indiceVirtual,indiceFisica, clock, procId):
    
    #print 'Indice da Pagina da Virtual que vai entrar: ' + str(indiceVirtual) 
    #print 'Indice da Pagina da Fisica que vai sair: ' + str(indiceFisica) 
    
    #ajusta pagina da memoria virtual
    #Marca que a pagina virtual vai estar pesente
    #mapeia a pagina da mem virtual na pagina da mem fisica
    mem_virtual.tabela[indiceVirtual].set_presente(1)
    mem_virtual.tabela[indiceVirtual].set_mapeada(indiceFisica)
    
    #ajusta pagina da memoria fisica
    #faz o mapeamento inverso
    #seta o bit r, clock e id do processo que usa a pagina
    mem_fisica.tabela[indiceFisica].set_mapeada(indiceVirtual)
    mem_fisica.tabela[indiceFisica].set_r(1)
    mem_fisica.tabela[indiceFisica].set_tAcesso(clock)
    mem_fisica.tabela[indiceFisica].set_procId(procId)
    
    #escreve no arquivo da memoria fisica
    
    #pega o tamanho da pagina
    qtde = mem_virtual.get_p()
    inicio = indiceFisica * qtde
    
    for i in range(qtde):
        pid = mem_virtual.readbin((indiceVirtual * qtde)+ i)
        mem_fisica.writebin(inicio + i,pid)
        mem_fisica.vetor[int(inicio) + i] = int(pid)
    
