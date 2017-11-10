from memory import *

def simula (intervalo,processos):
    for execucao in processos:
        if execucao[1] == 'COMPACTAR':
            print execucao
            compactar()
        else:
            executa(execucao)

def executa (execucao):
    print 'executando: ' + execucao[1].nome
    

