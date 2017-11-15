from memory import *
from operator import itemgetter
import time

# itera em uma lista de execucoes; 
def simula (intervalo,listaExecucao):
    clock = 0;
    count = 0
    execucao = listaExecucao[count]
    while True:
        print 'clock: ' + str(clock)
        if clock == execucao[0]:
            if isinstance(execucao[1], basestring):
                if execucao[1] == 'COMPACTAR':
                    compactar()
                else:
                    print 'chegou '+ execucao[1] + ' em t: ' + str(execucao[0])
                    mem_virtual.best_fit(execucao[4])
                    
            else:
                executa(execucao)
            count += 1
            if count == len(listaExecucao):
                break
            execucao = listaExecucao[count]
        else:
            clock +=1

# recebe os processos listos de um arquivo trace e 
# devolve uma lista ordenada por t0 com as execucoes
# os elementos da lista tem o formato:
# [t0,p, PID, <processo>] 
# [t0,nome,ocupa,PID,<processo>]  ou [t,'COMPACTAR', -1]
def lista_de_execucao(processos):
    listaExecucao = []
    for execucao in processos:
        if execucao[1] == 'COMPACTAR':
            listaExecucao.append([int(execucao[0]),execucao[1],-1])
        else:
            listaExecucao.append([execucao[1].t0,execucao[1].nome,execucao[1].ocupa,execucao[1].pid,execucao[1]])
            for acesso in execucao[1].acessos:
                listaExecucao.append([acesso[1],acesso[0], execucao[1].pid, execucao[1]])
    return sorted(listaExecucao,key=itemgetter(0));

def executa (execucao):
    print  'em t: ' + str(execucao[0]) + ' PID: ' + str(execucao[2]) + ' acessa posicao: ' + str(execucao[1])
   

def set_memorias(fisica,virtual):
    global mem_fisica
    global mem_virtual
    mem_fisica = fisica
    mem_virtual = virtual
