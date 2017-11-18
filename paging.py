# algoritmo de substituicao de paginas

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

def fin_fout(processo, acesso, clock, mem_fisica, mem_virtual):
    print 'First-In, First-Out'
    
    #verifica qual eh a paina mais velha alocada
    
    #pego o tempo da primeira pagina da tabela de paginas para comecar
    old = mem_fisica.tabela[0].get_tAcesso()
    i = 0
    for pagina in mem_fisica.tabela:
        if pagina.get_tAcesso() < old:
            old = pagina.get_tAcesso()
            remover = i
        i += 1
        
    substitui_pagina(processo, acesso, clock, remover, mem_fisica, mem_virtual)

def LRUv2():
    print 'Least Recentely Used (Segunda versao)'

def LRUv4():
    print 'Least Recentely Used (Quarta versao)'


# substitui a pagina de indice 'remover':
def substitui_pagina(proc, pos, clock, remover, mem_fisica, mem_virtual):

    # -> parei aqui! Tem que testar!
    pid = proc.get_pid()
    
    # pega a qual pagina aquela posicao acessada pertence
    tamPagina = mem_virtual.get_p()
    pagina = pos/tamPagina
        
    # 1) alterar a memoria virtual para que a pagina removida tenha o bit presente/ausente = 0
    indiceVirtual = mem_fisica.tabela[remover].get_mapeada()
    mem_virtual.tabela[indiceVirtual].set_presente(0)
    
    mem_virtual.tabela[pagina].set_presente(1)
    mem_virtual.tabela[pagina].set_mapeada(remover)
    
    
    # 2) alterar a pag da memoria fisica com os dados da pagina nova que vai entrar
    mem_fisica.tabela[remover].set_procId(pid)
    mem_fisica.tabela[remover].set_mapeada(pagina)
    mem_fisica.tabela[remover].set_r(1)
    mem_fisica.tabela[remover].set_tAcesso(clock)
    
    
