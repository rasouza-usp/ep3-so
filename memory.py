# algoritmos de gerencia de espaco livre

# o controle de espaco livre tem que ser feito com lista ligada: ver aula15.pdf
# Nao vai dar pra usar o bitmap
from struct import pack,unpack
from linkedlist import *


class Memory:
    def __init__ (self, total, s, p, filename):
        self.tamanho = total
        self.s = s
        self.p = p
        self.arquivo = filename
        
        #lista que vai espelhar a situacao da memoria. Vamos escrever essa lista no arquivo
        self.vetor = [-1] * self.tamanho 
        
        #lista ligada para controle do espaco livre da memoria
        self.lista = LinkedList('L',0,self.tamanho,None)
        
        #Abre o arquivo para a memoria
        self.memfile = open (filename,'wb')
        
        #define tamanho do arquivo binario em bytes
        # b signed char => 1 byte
        self.memfile.write(pack(str(self.tamanho)+'b',*self.vetor))
        self.memfile.flush()
		
    def __del__ (self):
        self.memfile.close()
    
    # escreve data (inteiro) na posicao position da memoria
    def writebin (self,position,data):
        self.memfile.seek(position);
        bindata = pack('1b',data)
        self.memfile.write(bindata)
        self.memfile.flush()
        
    def set_vetor(self,inicio,pid,qtde):
        i = 0
        while i < int(qtde):
            self.vetor[int(inicio) + i] = int(pid)
            i = i + 1
            
    #atualiza o arquivo de memoria de acordo com o vetor       
    def update_file(self):
        self.memfile = open (self.arquivo,'wb')
        self.memfile.write(pack(str(self.tamanho)+'b',*self.vetor))
        self.memfile.close()
            
       
    def get_lista(self):
		return self.lista

    # le a posicao pos do arquivo de memoria e devolve seu conteudo
    def readbin (self, filename, pos):
        fin = open(filename,"rb")
        fin.seek(pos)
        x = int(unpack('1b',fin.read(1))[0])
        fin.close()
        return x
    
    # imprime conteudo de toda a memoria
    def dump (self,filename):
        for i in range(self.tamanho):
            print('Posicao ' + str(i) + ' PID: ' +str(self.readbin(filename,i)))


#varre a lista ligada e procura o menor espaco vazio para alocar o processo
def best_fit(memoria,p):
    print 'best fit'
	
    lista = memoria.get_lista()
    #->>>Parte 1: encontra um espaco livre na lista ligada para o prcesso que chega  
    #verfica o espaco ocupado pelo processo
    ocupa = p.get_ocupa()
    
    #cria os elementos que varrem a lista
    current = lista.get_head()
    posicao = None

    #varre a lista e pega a menor posicao de tamanho livre e coloca em 'posicao'
    while current:
        if current.get_data() == 'L' and current.get_tamanho() >= ocupa:
            if posicao == None:
                posicao = current
            else:
                if current.get_tamanho() < posicao.get_tamanho():
                    posicao = current
        current = current.get_next()
     
    #pega onde a posicao escolhida se inicia e o tamanho
    ini = posicao.get_inicio()
    tam = posicao.get_tamanho()
	
    #caso a posicao encontrada seja do tamanho exato requerido
    if (posicao.get_tamanho() == ocupa):
        posicao.set_data('P')
        
    #Caso a posicao encontrada seja maior do que o suficiente
    else:
		
        #aloca um novo node para o processo que chega
        no = Node('P',ini,ocupa,posicao)
	
        #o no alterado tem um novo inicio e um novo tamanho	    
        posicao.set_inicio(int(ini + ocupa))
        posicao.set_tamanho(int(tam - ocupa))
	    
        #colocar o novo noh no lugar correto
        #caso o node alterado seja o primeiro da lista ligada
        if lista.get_head() == posicao:
            lista.set_head(no)
            posicao.set_previous(no)
			
		#caso seja necessario alterar qualquer outro ponto da lista
        else:
			posicao.get_previous().set_next(no)
			no.set_previous(posicao.get_previous())
			posicao.set_previous(no)
			
    #->>>Parte 2: Define base e limite para o processo alocado
    p.set_base(ini)
    p.set_limite(ini+ocupa-1)
    
    #->>>Parte 3: Altera o vetor da memoria de acordo com o espaco destinado ao novo processo
    pid = p.get_pid()
    memoria.set_vetor(ini,pid,ocupa)
    memoria.update_file()

def worst_fit():
    print 'worst fit'

def quick_fit():
    print 'quick fit'

def compactar():
    print 'compactando memoria'
