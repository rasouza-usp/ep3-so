# -*- coding: utf-8 -*-
#/*
# *
# * Bruno Ferrero n.USP: 3690142  Curso: BCC
# * Rodrigo Alves n.USP 6800149   Curso: BCC
# * Tais Pinheiro n.USP 7580421   Curso: BCC
# *
# * Data: Nov/2017
# *
# */

class Processo:
    current_pid = 0

    def __init__(self, t0, tf, b, nome, acessos):
        self.t0 = int(t0)         # tempo de chegada do processo
        self.tf = int(tf)         # tempo de termino do processo
        self.b = int(b)           # tamanho de memoria requisitado pelo processo
        self.nome = nome          # string com nome do processo
        self.ocupa = 0            # tamanho ocupado pelo processo devido a uniadade de alocacao (tamanho marcado com seu pid)
        self.reserva = 0          # tamanho reservado pelo processo devida ao tamanho da pagina  
        self.base = -1            # endereco base do processo
        self.limite = -1          # endereco limite do processo  
        self.setpid()             # define pid do processo
        self.setAcessos(acessos)  # pares de acesso a memoria (pn,tn)

    def setpid(self):
        self.pid = Processo.current_pid
        Processo.current_pid += 1
         
    def get_b(self):
        return self.b
        
    def get_ocupa(self):
        return self.ocupa
    
    def get_reserva(self):
        return self.reserva
        
    def get_base(self):
        return self.base
        
    def get_pid(self):
        return self.pid
        
    def get_limite(self):
        return self.limite
        
    def get_reserva(self):
        return self.reserva
        
    def set_base(self,base):
        self.base = int(base)
    
    def set_limite(self,limite):
        self.limite = int(limite)

    def set_ocupa(self,s):
        b = self.b
        if(b % s) == 0:
            self.ocupa = b
        else:
            self.ocupa = (b/s + 1) * s
    
    def set_reserva(self,p):
        b = self.ocupa
        if (b % p) == 0:
            self.reserva = b
        else:
            self.reserva = (b/p + 1) * p
    
    def show(self):
        print 'PID: ' + str(self.pid) + ' Nome:' + str(self.nome)
        
    def setAcessos(self, acessos):
        """ Pega o vetor de acessos a memória e organiza em pares (pn,tn) """
        acessos = map (int,acessos)
        self.acessos = zip(*[iter(acessos)]*2) 
