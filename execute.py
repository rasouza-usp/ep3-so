from memory import *

def simula (intervalo,processos):
    for execucao in processos:
        if execucao[1] == 'COMPACTAR':
            print execucao
            compactar()
        else:
            executa(execucao)

def executa (execucao):
    print 'executando: ' + execucao[1].nome + ' PID: ' + str(execucao[1].pid) 
    print  execucao[1].acessos
