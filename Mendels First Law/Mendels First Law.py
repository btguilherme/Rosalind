# -.- encoding:utf-8 -.-

'''
Autor: Guilherme Camargo
Titulo: Mendels First Law.py
Data: 23/05/16
Entrada: k, m, n (inteiros positivos)
Objetivo: Calcular a probabilidade de dois indivíduos selecionados
        aleatoriamente produzirem um indivíduo que possua um alelo dominante.
Saida: Valor menor ou igual a 1, representando a probabilidade.
Obs1.: k, m e n devem ser inteiros positivos.
Obs2.:  k representa número de indivíduos homozigotos dominantes (AA);
	m representa número de indivíduos heterozigotos e (Aa);
	n representa número de indivíduos homozigotos recessivos (aa).
'''

from __future__ import division
import sys
import Verifications as ver

def main():
    probs = {}
    k,m,n = 0,0,0
    if len(sys.argv) < 4:
        k,m,n = 2,2,2
    else:
        ver.verifyNumber(sys.argv[1],sys.argv[2],sys.argv[3])
        ver.verifySum(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
        ver.verifyPositivity(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
        k,m,n = int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])

    probs = calcProbabilities(k,m,n)
    print "k: ",k, "\tm: ",m,"\tn: ",n

    prob = (
        (1.00 * probs['AA-AA']) + (1.00 * probs['AA-Aa']) +
        (1.00 * probs['AA-aa']) + (0.75 * probs['Aa-Aa']) +
        (0.50 * probs['Aa-aa']) + (0.00 * probs['aa-aa']))

    print prob
    return

def calcProbabilities(k, m, n):
    total = k+m+n
    probs = {
        'AA-AA':((k/total) * ((k-1)/(total-1))),
        'AA-Aa':((k/total) * (m/(total-1))) + ((m/total) * (k/(total-1))),
        'AA-aa':((k/total) * (n/(total-1))) + ((n/total) * (k/(total-1))),
        'Aa-Aa':((m/total) * ((m-1)/(total-1))),
        'Aa-aa':((m/total) * (n/(total-1))) + ((n/total) * (m/(total-1))),
        'aa-aa':((n/total) * ((n-1)/(total-1)))
        }
    return probs

main()
