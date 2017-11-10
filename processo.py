# -*- coding: utf-8 -*-

class Processo:
    current_pid = 0

    def __init__(self, t0, tf, b, nome, acessos):
        self.t0 = int(t0)
        self.tf = int(tf)
        self.b = int(b)
        self.nome = nome
        self.setpid()
        self.setAcessos(acessos)

    def setpid(self):
        self.pid = Processo.current_pid
        Processo.current_pid += 1

    def setAcessos(self, acessos):
        """ Pega o vetor de acessos a memória e organiza em pares (pn,tn) """
        acessos = map (int,acessos)
        self.acessos = zip(*[iter(acessos)]*2) # TODO: Converter as strings para inteiros: Done
