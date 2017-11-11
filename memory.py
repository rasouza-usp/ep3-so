# algoritmos de gerencia de espaco livre

# o controle de espaco livre tem que ser feito com lista ligada: ver aula15.pdf
# Nao vai dar pra usar o bitmap
from struct import pack
from linkedlist import *

class Memory:
    def __init__ (self, total, s, p, filename):
        self.tamanho = total
        self.s = s
        self.p = p
        
        #vetor que vai espelhar a situacao da memoria. Vams escrever esse vetor no arquivo
        self.vetor = [] 
        
        #lista ligada para controle do espaco livre da memoria
        self.lista = LinkedList('L',0,self.tamanho,None)
        
        #Abre o arquivo para escrota binara
        self.memfile = open (filename,"wb")
        
        #define tamanho do arquivo binario em bytes
        for i in range(self.tamanho):
            self.memfile.write(pack('i',-1))
            self.vetor.append(-1)
        self.memfile.seek(self.tamanho-1)
        self.memfile.write("\0")
        self.memfile.close()
		
    def __del__ (self):
        self.memfile.close()

def best_fit():
    print 'best fit'

def worst_fit():
    print 'worst fit'

def quick_fit():
    print 'quick fit'

def compactar():
    print 'compactando memoria'
