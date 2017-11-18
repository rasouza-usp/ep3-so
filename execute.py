from memory import *
from operator import itemgetter
import time
    
    
# itera em uma lista de execucoes; 
def simula (intervalo,listaExecucao,espaco,substitui):
    global clock
    global pagefault
    
    clock = 0
    count = 0 
    pagefault = 0
    execucao = listaExecucao[count]
    
    while True:
        print 'clock: ' + str(clock)
        if clock == execucao[0]:
            if isinstance(execucao[1], basestring):
                if execucao[1] == 'COMPACTAR':
                    print 'compactando memoria'
                    #compactar()
                elif False:
                    # Aqui vamos tratar o caso de remover um processo
                    remover_processo()
                else:
                    # Chegou um novo processo: manda pra memoria virtual
                    print 'chegou '+ execucao[1] + ' em t: ' + str(execucao[0])
                    if espaco == 1:
                        mem_virtual.best_fit(execucao[4])
                    elif espaco == 2:
                        mem_virtual.worst_fit(execucao[4])
                    elif espaco == 3:
                        mem_virtual.quick_fit(execucao[4])
                        
                    mem_virtual.get_pagina(execucao[4])
                    print 'olha as tabelas: '
                    #na hora do acesso varre a mem fisica e proc espaco se nao
                    #mem_virtual.lista.show()
                    #mem_virtual.show_tabela()
            else:
                # acesso a memoria
                executa(execucao)
            count += 1
            if count == len(listaExecucao):
                break
            execucao = listaExecucao[count]
        else:
            clock +=1
        
        print 'MEMORIA VIRTUAL'    
        mem_virtual.show_tabela()
        print 'MEMORIA FISICA'    
        mem_fisica.show_tabela()
        

# recebe os processos lidos de um arquivo trace e 
# devolve uma lista ordenada por t0 com todos os acessos a memoria
# os elementos da lista tem o formato:
# [t0,p, PID, <processo>] 
# [t0,nome,ocupa,PID,<processo>]  ou [t,'COMPACTAR', -1] ! podemos tirar esse -1 do 'COMPACTAR'
def lista_de_execucao(processos):
    listaExecucao = []
    for execucao in processos:
        if execucao[1] == 'COMPACTAR':
            listaExecucao.append([execucao[0],execucao[1],-1])
        else:
            listaExecucao.append([execucao[1].t0,execucao[1].nome,execucao[1].ocupa,execucao[1].pid,execucao[1]])
            # adicionar tf para remover o processo
            #listaExecucao.append([execucao[1].tf,'REMOVER',execucao[1]])
            for acesso in execucao[1].acessos:
                listaExecucao.append([acesso[1],acesso[0], execucao[1].pid, execucao[1]])
    return sorted(listaExecucao,key=itemgetter(0));

# estrutura: [t0,p, PID, <processo>] 
def executa (execucao):
    print  'em t: ' + str(execucao[0]) + ' PID: ' + str(execucao[2]) + ' acessa posicao: ' + str(execucao[1])
    
    global pagefault
    
    # encontra a posicao acessada = base + p
    pos = execucao[3].get_base()+execucao[1]
    pid = execucao[3].get_pid()
    
    # pega a qual pagina aquela posicao pertence
    tamPagina = mem_virtual.get_p()
    pagina = pos/tamPagina
    
    # verifica se a pagina se encontra na memoria fisica
    
    #caso nao esteja:
    if mem_virtual.tabela[pagina].get_presente() == 0:

       #pagefault
        pagefault +=1
        alocou = 0
        
        # passo 1: verifica se existe espaco livre na mem fisica pra mapear a pag
        
        # pega o numero de paginas na memoria fisica
        numPags = int(mem_fisica.get_tamanho()/tamPagina)
        
        i = 0
        
        while i < numPags:

            #se existe uma pagina disponivel:
            if mem_fisica.tabela[i].get_procId() == -1:

                #altera os dados da pagina na mem fisica:
                mem_fisica.tabela[i].set_procId(pid)
                mem_fisica.tabela[i].set_r(1)
                mem_fisica.tabela[i].set_tAcesso(clock)
                mem_fisica.tabela[i].set_mapeada(pagina)
                
                #altera o bit presente/ausente
                mem_virtual.tabela[pagina].set_presente(1)
                
                #grava o mapeamento a memoria virtual na fisica
                mem_virtual.tabela[pagina].set_mapeada(i)
                
                alocou = 1
                i = numPags
            i +=1
    
    # se verificamos que toda a memoria fisica e nao encontrou espaco
    #if alocou == 0:
                
    #Usando algoritmos de paginacao
    
    
   
def set_memorias(fisica,virtual):
    global mem_fisica
    global mem_virtual

    mem_fisica = fisica
    mem_virtual = virtual
    
