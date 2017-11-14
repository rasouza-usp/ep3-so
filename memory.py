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

#varre a lista liga e procura o menor espaco vazio para alocar o processo
def best_fit(mem_virtual,p):
    print 'best fit'
    
    #verfica o numero de unidades ocupada pelo processo
    ocupa = p.get_ocupa()
    
    #cria os elementos que varrem a lista
    current = mem_virtual.head
    posicao = current

    #varre a lista e pega a menor posicao de tramanho livre em 'posicao'
    while current:
        if current.get_data() == 'L' and current.get_tamanho() >=  ocupa and current.get_tamanho < posicao.get_tamanho():
            posicao = current
        current = current.get_next()
	
	#Caso a posiacao encontrada seja maior do que o suficiente
	if(posicao.get_tamanho > ocupa):
	    #aloca um novo node para o processo que chega
	    no = Node('P',posicao.get_inicio(),ocupa,posicao)
	
	    #o no alterado tem um novo inicio
	    ini = posicao.get_inicio()
	    tam = posicao.get_tamanho()
	    posicao.set_inicio(ocupa + ini)
	    posicao.set_tamanho(tam-ocupa)
	    
	    #colocar o novo noh no lugar correto
	    #doing
	    
	#caso a posicao encontrada seja do tamanho exato requerido
	else:
		posicao.set_data('P')
	
	
    return posicao
    

def worst_fit():
    print 'worst fit'

def quick_fit():
    print 'quick fit'

def compactar():
    print 'compactando memoria'
