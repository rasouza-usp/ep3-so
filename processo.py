# -*- coding: utf-8 -*-

class Processo:
    current_pid = 0

    def __init__(self, t0, tf, b, nome, acessos):
        self.t0 = int(t0)
        self.tf = int(tf)
        self.b = int(b)
        self.nome = nome
        self.ocupa = 0
        self.setpid()
        self.setAcessos(acessos)

    def setpid(self):
        self.pid = Processo.current_pid
        Processo.current_pid += 1
         
    def get_b(self):
        return self.b
        
    def get_ocupa(self):
        return self.ocupa

    def set_ocupa(self,s):
        b = self.get_b
        if(b % s) == 0:
            self.ocupa = b
        else:
            self.ocupa = (b/s + 1) * s

    def setAcessos(self, acessos):
        """ Pega o vetor de acessos a memória e organiza em pares (pn,tn) """
        acessos = map (int,acessos)
        self.acessos = zip(*[iter(acessos)]*2) 
