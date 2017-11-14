# -*- coding: utf-8 -*-

import os
import sys
import Queue

from processo import *
from memory import *
import paging as pg
import execute as ex
import readline

# Globals
memoria = {
    "total": 0,
    "virtual": 0,
    "s": 0,
    "p": 0
}
espacos = {1: 'Best Fit', 
           2: 'Worst Fit', 
           3: 'Quick Fit'
}
paginacao = {1: 'Optimal', 
             2: 'First In, First Out', 
             3: 'Least Recently Used v2', 
             4: 'Least Recently Used v4'
}

processos = [] # Lista de processos na forma (t0, Processo)
espaco = 1 # Algoritmo de gerenciamento espaço livre
substitui = 1 # Algoritmo de substituição de páginas

### MAIN
def main ():
    if len(sys.argv) == 1: 
        terminal() # Executar sem argumentos passa a ser um terminal
    elif len(sys.argv) != 4: 
        help() # Executar sem todos os argumentos necessários mostra ajuda

    # DEBUG ---
    carrega(sys.argv[1])
    #print vars(processos[0][1])
    # END DEBUG ---
    mem_fisica = Memory(int(memoria['total']),int(memoria['s']),int(memoria['p']),'/tmp/ep3.mem')
    mem_virtual = Memory(int(memoria['virtual']),int(memoria['s']),int(memoria['p']),'/tmp/ep3.vir')
    #mem_fisica.dump('/tmp/ep3.mem')
    # os elementos da lista tem o formato:
    # [t0,p, PID] 
    # [t0,nome,PID]  ou [t,'COMPACTAR', -1]
    listaExecucao = ex.lista_de_execucao(processos)
    ex.simula (1,listaExecucao)

# Funções
def help(): 
    print """[USO] python ep3.py ARQUIVO ESPACO SUBSTITUI

    ARQUIVO - caminho do arquivo trace
    ESPACO - algoritmo de gerenciamento de espaco livre
    SUBSTITUI - algoritmo de substituicao de pagina"""

def set_espaco(algoritmo):
    global espaco
    espaco = algoritmo

def set_substitui(algoritmo):
    global substitui
    substitui = algoritmo

def carrega(arquivo):
    try:
        f = open(arquivo, "r")
    except IOError:
        print "Nao achou o arquivo"
        return
        
    global mem_fisica
    global mem_virtual

    # Define parametros da memória
    memoria["total"], memoria["virtual"], memoria["s"], memoria["p"] = f.readline().split()
    
    #Cria os arquivos de memoria
    mem_fisica = Memory(int(memoria['total']),int(memoria['s']),int(memoria['p']),'/tmp/ep3.mem')
    mem_virtual = Memory(int(memoria['virtual']),int(memoria['s']),int(memoria['p']),'/tmp/ep3.vir')
    
    #mem_fisica.lista.show()
    #mem_fisica.dump('/tmp/ep3.mem')
    #mem_virtual.lista.show()
	
    # Timeline dos processos na memória
    for line in f: 
        line = line.split()
        if line[1] != "COMPACTAR":
            p = Processo(line[0], line[1], line[2], line[3], line[4:]) # Cria um processo
            p.set_ocupa(int(memoria["s"]))
            processos.append((line[0],p)) # Coloca na lista de processos
        else:
            processos.append((line[0], line[1]))
    f.close()


def terminal():
    while(True):
        command = (raw_input('[ep3]: ')).strip().split()
        print command 
        if command[0] == "sai": sys.exit(0)
        if command[0] == "carrega":carrega(command[1])        
        if command[0] == "espaco": set_espaco(command[1])
        if command[0] == "substitui": set_substitui(command[1])
        if command[0] == "executa": ex.simula(command[1],processos)

if __name__ == "__main__":
    main()
