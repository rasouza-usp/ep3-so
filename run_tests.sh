#!/usr/bin/env bash
#
# Faz 30 execucoes de um arquivo trace 
# para todas as combinacoes de algoritmos de paginacao e de espaco livre
#
#

# best-fit & First In, First Out 
results='' 
for i in `seq 1 30`; do
    tempo=`python ep3.py teste.txt 1 2 | grep 'Tempo' | awk '{print $NF}'`
    results=${results}'  '${tempo} 
done
PAGEFAULT=`python ep3.py teste.txt 1 2 | grep 'Pagefault' | awk '{print $NF}'`

media_std=$(
    for i in  ${results}; do echo $i;done |
        awk '{sum+=$1; sumsq+=$1*$1}END{print sum/NR " " sqrt(sumsq/NR - (sum/NR)**2)}'
)

echo "best-fit & First In, First Out" 
echo "media | std"
echo ${media_std}
echo "Pagefault: " $PAGEFAULT

# best-fit & LRUv2
results='' 
for i in `seq 1 30`; do
    tempo=`python ep3.py teste.txt 1 3 | grep 'Tempo' | awk '{print $NF}'`
    results=${results}'  '${tempo} 
done
PAGEFAULT=`python ep3.py teste.txt 1 3 | grep 'Pagefault' | awk '{print $NF}'`

media_std=$(
    for i in  ${results}; do echo $i;done |
        awk '{sum+=$1; sumsq+=$1*$1}END{print sum/NR " " sqrt(sumsq/NR - (sum/NR)**2)}'
)

echo "best-fit & LRUv2" 
echo "media | std"
echo ${media_std}
echo "Pagefault: " $PAGEFAULT


# best-fit & LRUv4
esults='' 
for i in `seq 1 30`; do
    tempo=`python ep3.py teste.txt 1 4 | grep 'Tempo' | awk '{print $NF}'`
    results=${results}'  '${tempo} 
done
PAGEFAULT=`python ep3.py teste.txt 1 4 | grep 'Pagefault' | awk '{print $NF}'`

media_std=$(
    for i in  ${results}; do echo $i;done |
        awk '{sum+=$1; sumsq+=$1*$1}END{print sum/NR " " sqrt(sumsq/NR - (sum/NR)**2)}'
)

echo "best-fit & LRUv4" 
echo "media | std"
echo ${media_std}
echo "Pagefault: " $PAGEFAULT

# worst-fit & First In, First Out 
results='' 
for i in `seq 1 30`; do
    tempo=`python ep3.py teste.txt 2 2 | grep 'Tempo' | awk '{print $NF}'`
    results=${results}'  '${tempo} 
done
PAGEFAULT=`python ep3.py teste.txt 2 2 | grep 'Pagefault' | awk '{print $NF}'`

media_std=$(
    for i in  ${results}; do echo $i;done |
        awk '{sum+=$1; sumsq+=$1*$1}END{print sum/NR " " sqrt(sumsq/NR - (sum/NR)**2)}'
)

echo "worst-fit & First In, First Out" 
echo "media | std"
echo ${media_std}
echo "Pagefault: " $PAGEFAULT

# worst-fit & LRUv2
results='' 
for i in `seq 1 30`; do
    tempo=`python ep3.py teste.txt 2 3 | grep 'Tempo' | awk '{print $NF}'`
    results=${results}'  '${tempo} 
done
PAGEFAULT=`python ep3.py teste.txt 2 3 | grep 'Pagefault' | awk '{print $NF}'`

media_std=$(
    for i in  ${results}; do echo $i;done |
        awk '{sum+=$1; sumsq+=$1*$1}END{print sum/NR " " sqrt(sumsq/NR - (sum/NR)**2)}'
)

echo "worst-fit & LRUv2" 
echo "media | std"
echo ${media_std}
echo "Pagefault: " $PAGEFAULT


# worst-fit & LRUv4
esults='' 
for i in `seq 1 30`; do
    tempo=`python ep3.py teste.txt 2 4 | grep 'Tempo' | awk '{print $NF}'`
    results=${results}'  '${tempo} 
done
PAGEFAULT=`python ep3.py teste.txt 2 4 | grep 'Pagefault' | awk '{print $NF}'`

media_std=$(
    for i in  ${results}; do echo $i;done |
        awk '{sum+=$1; sumsq+=$1*$1}END{print sum/NR " " sqrt(sumsq/NR - (sum/NR)**2)}'
)

echo "worst-fit & LRUv4" 
echo "media | std"
echo ${media_std}
echo "Pagefault: " $PAGEFAULT
