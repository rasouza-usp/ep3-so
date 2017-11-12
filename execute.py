from memory import *
import time

def simula (intervalo,processos):
	
    for execucao in processos:
        if execucao[1] == 'COMPACTAR' and clock == execucao[0]:
            print execucao
            compactar()
                
        else:
            executa(execucao)

         

def executa (execucao):
    print 'executando: ' + execucao[1].nome + ' PID: ' + str(execucao[1].pid)
    print  execucao[1].acessos
    
		
