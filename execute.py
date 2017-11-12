from memory import *
import time

def simula (intervalo,processos):
	global clock
	clock = -1
	go = 1
	
	while go == 1:
		k = 0
        for execucao in processos:
            if execucao[1] == 'COMPACTAR' and clock == execucao[0]:
                print execucao
                compactar()
                del processos[k]
                
            else:
                executa(execucao)
            k += 1 
        clock = += 1
        go = 0   

def executa (execucao):
    print 'executando: ' + execucao[1].nome + ' PID: ' + str(execucao[1].pid)
    print  execucao[1].acessos
    #verifica se eh hora de comecar a rodar
    if execucao[0] == clock:
		#identifica que o processo ja foi iniciado
		execucao[1].started = 1
	#verifica se tem algum acesso para aquele instante
    
		
