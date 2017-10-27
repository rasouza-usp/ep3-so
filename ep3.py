# -*- coding: utf-8 -*-

import os
import sys
import Queue

from processo import *

# Globals
mem = {
    "total": 0,
    "virtual": 0,
    "s": 0,
    "p": 0
}

processos = [] # Lista de processos na forma (t0, Processo)
espaco = 1 # Algoritmo de gerenciamento espaço livre
substitui = 1 # Algoritmo de substituição de páginas

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
    f = open(arquivo, "r")

    # Define parametros da memória
    mem["total"], mem["virtual"], mem["s"], mem["p"] = f.readline().split()

    # Timeline dos processos na memória
    for line in f: 
        line = line.split()
        if line[1] != "COMPACTAR":
            p = Processo(line[0], line[1], line[2], line[3], line[4:]) # Cria um processo
            processos.append((line[0],p)) # Coloca na lista de processos
        else:
            processos.append((line[0], line[1]))

def terminal():
    while(True):
        command = (raw_input('[ep3]: ')).strip().split()
    
        if command[0] == "sai": sys.exit(0)
        if command[0] == "carrega": carrega(command[1])
        if command[0] == "espaco": set_espaco(command[1])
        if command[0] == "substitui": set_substitui(command[1])
        if command[0] == "executa": executa(command[1])

### MAIN

if len(sys.argv) == 1: terminal() # Executar sem argumentos passa a ser um terminal
elif len(sys.argv) != 4: help() # Executar sem todos os argumentos necessários mostra ajuda

mem_fisica = open("/tmp/ep3.mem", "w")
mem_virtual = open("/tmp/ep3.vir", "w")

# DEBUG ---
carrega(sys.argv[1])
print vars(processos[0][1])

# END DEBUG ---