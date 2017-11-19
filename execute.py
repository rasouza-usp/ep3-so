from memory import *
from paging import *
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
        #print 'clock: ' + str(clock)
        if clock == execucao[0]:
            if isinstance(execucao[1], basestring):
                #print execucao
                if execucao[1] == 'COMPACTAR':
                    print 't: ' + str(execucao[0]) + ' COMPACTAR'
                    #compactar()
                elif execucao[1] == 'REMOVER':
                    # Aqui vamos tratar o caso de remover um processo
                    mem_virtual.remover_processo(execucao[3],mem_fisica)
                    #mem_virtual.lista.show()
                    #mem_virtual.dump()
                elif execucao[1] == 'ALOCAR':
                    # Chegou um novo processo: manda pra memoria virtual
                    print "t: " + str(execucao[0]) + ' ' + execucao[1] + ' para ' + execucao[3].nome 
                    if espaco == 1:
                        mem_virtual.best_fit(execucao[3])
                    elif espaco == 2:
                        mem_virtual.worst_fit(execucao[3])
                    elif espaco == 3:
                        mem_virtual.quick_fit(execucao[3])
                        
                    mem_virtual.get_pagina(execucao[3])
                    #print 'olha as tabelas: '
                    #na hora do acesso varre a mem fisica e proc espaco se nao
                    #mem_virtual.lista.show()
                    #mem_virtual.dump()
                    #mem_fisica.dump()
                elif execucao[1] == 'ACESSO':
                    # executa acesso a memoria
                    executa(execucao,substitui)
                    #mem_virtual.show_tabela()
                count += 1
                if count == len(listaExecucao):
                    break
                execucao = listaExecucao[count]
        else:
            clock +=1
            
# recebe os processos lidos de um arquivo trace e 
# devolve uma lista ordenada por t com todas ACOES de manipualacao da memoria
# os elementos da lista tem o seguinte formato:
# [ t, ACAO, tam/pos memoria, <processo>]
def lista_de_execucao(processos):
    listaExecucao = []
    for execucao in processos:
        if execucao[1] == 'COMPACTAR':
            listaExecucao.append([execucao[0],execucao[1],-1])
        else:
            listaExecucao.append([execucao[1].t0,"ALOCAR",execucao[1].ocupa,execucao[1]])
            for acesso in execucao[1].acessos:
                listaExecucao.append([acesso[1],'ACESSO',acesso[0],execucao[1]])
            # adicionar tf para remover o processo
            listaExecucao.append([execucao[1].tf,'REMOVER',-1,execucao[1]])
    return sorted(listaExecucao,key=itemgetter(0));

# [ t, ACAO, pos memoria, <processo>]
def executa (execucao,substitui):
    print "t: " + str(execucao[0]) + ' ' + execucao[1] + ' de ' + execucao[3].nome + ' em: ' + str(execucao[2])
    
    global pagefault
    
    # encontra a posicao acessada = base + p
    pos = execucao[3].get_base()+execucao[2]
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
        # busca espaco de uma pagina vazia na memoria
        for i in range(numPags):
            #se existe uma pagina disponivel:
            if mem_fisica.tabela[i].get_procId() == -1:
                
                print "\n\n\n"
                print "PID: " + str(pid) + " foi pra pagina: " + str(i) + " da memoria fisica\n\n" 
                
                mapeia_virtual_to_fisica(mem_virtual,mem_fisica,pagina,i, clock, pid)
                
                # alocou a pagina; pode sair do loop
                alocou = 1
                break
        
        # se nao consegui alocar a pagina, then ...
        # Usando algoritmos de paginacao
        if alocou == 0:
            print 'Pagina quer entrar'
            mem_virtual.tabela[pagina].show()
            if substitui == 1:
                print 'Optimal'
            elif substitui == 2:
                print 'First in First Out'
                fin_fout(mem_virtual,mem_fisica,pagina,clock,pid)
            elif substitui == 3:
                print 'LRUv2'
            elif substitui == 4:
                print 'LRUv4'
        #mem_fisica.show_tabela()

def set_memorias(fisica,virtual):
    global mem_fisica
    global mem_virtual

    mem_fisica = fisica
    mem_virtual = virtual
