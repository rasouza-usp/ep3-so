# -*- coding: utf-8 -*-

import os
import sys

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

processos = []  # Lista de processos na forma (t0, Processo)
espaco = 1      # Algoritmo de gerenciamento espaço livre
substitui = 1   # Algoritmo de substituição de páginas


### MAIN
def main ():
    if len(sys.argv) == 1: 
        terminal()  # Executar sem argumentos passa a ser um terminal
    elif len(sys.argv) != 4: 
        help()      # Executar sem todos os argumentos necessários mostra ajuda
        sys.exit()
    
    # BATCH MODE ---
    carrega(sys.argv[1])
    set_espaco(int(sys.argv[2]))
    set_substitui(int(sys.argv[3]))
    listaExecucao = ex.lista_de_execucao(processos)
    ex.simula (1,listaExecucao,espaco,substitui)
    # END BATCH MODE ---

# Funções
def help(): 
    print """[USO MODO BATCH] python ep3.py ARQUIVO ESPACO SUBSTITUI

    ARQUIVO - caminho do arquivo trace
    ESPACO - algoritmo de gerenciamento de espaco livre
    SUBSTITUI - algoritmo de substituicao de pagina

[USO MODO INTERATIVO] python ep3.py
[ep3]: <comandos>
"""

def set_espaco(algoritmo):
    global espaco
    espaco = algoritmo

def set_substitui(algoritmo):
    global substitui
    substitui = algoritmo

# carrega arquivo trace em uma lista de Processos
def carrega(arquivo):
    try:
        f = open(arquivo, "r")
    except IOError:
        print "Nao achou o arquivo"
        return
        
    global mem_fisica
    global mem_virtual
    global tamanhos
    global processos
    
    processos = []
    tamanhos = []

    # Define parametros da memória
    memoria["total"], memoria["virtual"], memoria["s"], memoria["p"] = f.readline().split()
    
    #Cria os arquivos de memoria
    mem_fisica = Memory(int(memoria['total']),int(memoria['s']),int(memoria['p']),'/tmp/ep3.mem')
    mem_virtual = Memory(int(memoria['virtual']),int(memoria['s']),int(memoria['p']),'/tmp/ep3.vir')
    ex.set_memorias(mem_fisica,mem_virtual)

    # Timeline dos processos na memória
    for line in f: 
        line = line.split()
        if line[1] != "COMPACTAR":
            #Processo(t0, tf, b, nome, acessos)
            p = Processo(int(line[0]), int(line[1]), int(line[2]), line[3], line[4:]) # Cria um processo
            # define os tamanhos de que serao reservados para o processo 
            p.set_ocupa(int(memoria["s"]))
            p.set_reserva(int(memoria["p"]))
            # Coloca na lista de processos que sera ordenada por ordem de eventos
            processos.append((int(line[0]),p)) 
            #guarda os tamanhos para ser usado no quick fit
            tamanhos.append(p.get_reserva())
        else:
            processos.append((int(line[0]), line[1]))
    f.close()

# modo terminal
def terminal():
    while(True):
        command = (raw_input('[ep3]: ')).strip().split()
        if command:
            if command[0] == "sai": 
                sys.exit(0)
            if command[0] == "carrega":
                arquivo = command[1]
            if command[0] == "espaco":
                espaco = int(command[1])
            if command[0] == "substitui": 
                substitui = int(command[1])
            if command[0] == "executa":
                intervalo = int(command[1])
                carrega(arquivo)
                set_espaco(espaco)
                set_substitui(substitui)
                print 'Simulando: \nESPACO: ' + espacos[espaco] + ' | PAGINACAO: ' + paginacao[substitui]
                listaExecucao = ex.lista_de_execucao(processos)
                ex.simula (intervalo,listaExecucao,espaco,substitui)
                listaExecucao = []

if __name__ == "__main__":
    main()
