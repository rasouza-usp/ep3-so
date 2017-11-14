# -*- coding: utf-8 -*-

class Processo:
    current_pid = 0

    def __init__(self, t0, tf, b, nome, acessos):
        self.t0 = int(t0)
        self.tf = int(tf)
        self.b = int(b)
        self.nome = nome
        self.ocupa = 0
        self.base = -1
        self.limite = -1
        self.setpid()
        self.setAcessos(acessos)

    def setpid(self):
        self.pid = Processo.current_pid
        Processo.current_pid += 1
         
    def get_b(self):
        return self.b
        
    def get_ocupa(self):
        return self.ocupa
        
    def get_base(self):
        return self.base
        
    def get_limite(self):
        return self.limite
        
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

    def setAcessos(self, acessos):
        """ Pega o vetor de acessos a memória e organiza em pares (pn,tn) """
        acessos = map (int,acessos)
        self.acessos = zip(*[iter(acessos)]*2) 
