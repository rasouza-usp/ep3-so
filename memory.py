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
        self.memfile.close()
		
    def __del__ (self):
        self.memfile.close()

    def dump (self,filename):
        print ('Dump do arquivo ' + filename)
        fin = open(filename,'rb')
        for i in range(self.tamanho):
            print('Posicao ' + str(i) + ' PID: ' +str(unpack('b',fin.read(1)))) 

def best_fit():
    print 'best fit'

def worst_fit():
    print 'worst fit'

def quick_fit():
    print 'quick fit'

def compactar():
    print 'compactando memoria'
