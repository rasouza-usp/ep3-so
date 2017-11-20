#/*
# *
# * Bruno Ferrero n.USP: 3690142  Curso: BCC
# * Rodrigo Alves n.USP 6800149   Curso: BCC
# * Taís Pinheiro n.USP 7580421   Curso: BCC
# *
# * Data: Nov/2017
# *
# */

from memory import *
from paging import *
from operator import itemgetter
import time

# itera em uma lista de execucoes; 
def simula (intervalo,listaExecucao,espaco,substitui):
    global clock
    global pagefault
    global matriz_LRUv2

    timetotal = 0;
    t_i = 0
    t_f = 0

    if substitui == 3:
         global matriz_LRUv2
         npaginas = int(mem_fisica.get_tamanho()/mem_fisica.get_p())
         matriz_LRUv2 = matriz_LRUv2_init(npaginas)
    
    clock = 0
    count = 0 
    pagefault = 0
    execucao = listaExecucao[count]
    
    while True:
        if clock == execucao[0]:
            if isinstance(execucao[1], basestring):
                #print execucao
                if execucao[1] == 'COMPACTAR':
                    print 't: ' + str(execucao[0]) + ' COMPACTAR'
                    #compactar()
                elif execucao[1] == 'REMOVER':
                    # Aqui vamos tratar o caso de remover um processo
                    mem_virtual.remover_processo(execucao[3],mem_fisica)
                elif execucao[1] == 'ALOCAR':
                    # Chegou um novo processo: manda pra memoria virtual
                    print "t: " + str(execucao[0]) + ' ' + execucao[1] + ' para ' + execucao[3].nome
                    # disparando o cronometro 
                    t_i = time.time()
                    if espaco == 1:
                        mem_virtual.best_fit(execucao[3])
                    elif espaco == 2:
                        mem_virtual.worst_fit(execucao[3])
                    elif espaco == 3:
                        mem_virtual.quick_fit(execucao[3])
                    #carrega processo na tabela de pagina (mem virtual)
                    mem_virtual.set_pagina_tabela (execucao[3])
                    # para o cronometro e soma o tempo
                    t_f = time.time()
                    timetotal += (t_f - t_i)
                elif execucao[1] == 'ACESSO':
                    # disparando o cronometro 
                    t_i = time.time()
                    # executa ACESSO a memoria
                    executa(execucao,substitui)
                    # para o cronometro e soma o tempo
                    t_f = time.time()
                    timetotal += (t_f - t_i)
                count += 1
                if count == len(listaExecucao):
                    print 'Fim da Simulacao em t: ' + str(clock)
                    print 'Estado da Memoria Virtual em t: ' + str(clock)
                    mem_virtual.dump()
                    print 'Estado da Memoria Fisica em t: ' + str(clock)
                    mem_fisica.dump()
                    break
                execucao = listaExecucao[count]
        else:
            # imprime de <intervalo> em <intervalo>
            if clock%intervalo == 0:
                print ''
                print 'Estado da Memoria Virtual em t: ' + str(clock)
                mem_virtual.dump_status()
                print 'Bit Map da Memoria Virtual em t: ' + str(clock)
                mem_virtual.dump()
                print ''
                print 'Estado da Memoria Fisica em t: ' + str(clock)
                mem_fisica.dump_status()
                print 'Bit Map da Memoria Fisca em t: ' + str(clock)
                mem_fisica.dump()
            clock +=1
    
    print 'Tempo para encontrar espacos na memoria durante toda simulacao: ' + str(timetotal)
    print '# Pagefault: ' + str(pagefault)
            
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

# executa um ACESSO a memoria
# [tn, ACESSO, pn, <processo>]
def executa (execucao, substitui):
    print "t: " + str(execucao[0]) + ' ' + execucao[1] + ' de ' + execucao[3].nome + ' em: ' + str(execucao[2])
    
    global pagefault
    global matriz_LRUv2
    
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
        # pega o numero de paginas na memoria fisica
        numPags = int(mem_fisica.get_tamanho()/tamPagina)
        # passo 1: verifica se existe espaco livre na mem fisica pra mapear a pag
        # busca espaco de uma pagina vazia na memoria
        for i in range(numPags):
            #se existe uma pagina disponivel:
            if mem_fisica.tabela[i].get_procId() == -1:
                #print "PID: " + str(pid) + " foi pra pagina: " + str(i) + " da memoria fisica" 
                mapeia_virtual_to_fisica(mem_virtual,mem_fisica,pagina,i, clock, pid)                
                
                # se LRUv2 marcar acesso da pagina na matriz de acesso
                if substitui  == 3:
                    matriz_LRUv2 = marca_matriz(i,numPags,matriz_LRUv2)                
                # se LRUv4 marcar acesso da pagina no contador de acesso da pagina
                # vai levar em consideracao os ultimos 6 acessos
                elif substitui == 4:
                    mem_fisica.tabela[i].set_countLRUv4(6)

                # alocou a pagina; pode sair do loop
                alocou = 1
                break
        
        # se nao conseguiu alocar a pagina, then ...
        # Usando algoritmos de paginacao
        if alocou == 0:
            #print 'Pagina quer entrar'
            #mem_virtual.tabela[pagina].show()
            if substitui == 1:
                print 'Optimal'
            elif substitui == 2:
                fin_fout (mem_virtual,mem_fisica,pagina,clock,pid)
            elif substitui == 3:
                LRUv2 (mem_virtual,mem_fisica,pagina,clock,pid)
            elif substitui == 4:
                LRUv4 (mem_virtual,mem_fisica,pagina,clock,pid)
        #mem_fisica.show_tabela()

def set_memorias(fisica,virtual):
    global mem_fisica
    global mem_virtual
    mem_fisica = fisica
    mem_virtual = virtual
