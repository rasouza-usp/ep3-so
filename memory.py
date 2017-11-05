# algoritmos de gerencia de espaco livre
#https://pypi.python.org/pypi/bitarray
from bitarray import bitarray

## a memoria sera simulada com um bitarray

class Memory:
    def __init__ (self, total, s, p, filename):
        self.tamanho = total
        self.s = s
        self.p = p
        self.memoria = bitarray(total)
        self.memfile = open (filename,"wb")

    def __del__ (self):
        self.memfile.close()

def best_fit():
    print 'best fit'

def worst_fit():
    print 'worst fit'

def quick_fit():
    print 'quick fit'
