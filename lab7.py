# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:41:57 2017

@author: palkjaku
"""

def primeEratostenes(n):
    if (n < 2): return -1
    primes = [i+1 for i in range(n)]  #init tablicy liczb
    primes.remove(1)  #usuwamy 1
    j = 0  #counter while
    while j < len(primes):
        numberToCheck = primes[j]
        multipleOfValue = 1
        while True:
            #Liczymy aktualną wielokrotność
            multipleOfValue += 1
            searchNum = multipleOfValue * numberToCheck
            if searchNum <= n:
                if searchNum in primes:
                    primes.remove(searchNum)
            else:
                break
        j += 1
    return primes

    


def removePrimeNumber(lista,pierwsze):
    lista.sort()
    checkingNumber=0
    count=0
    wynikowa = ""
    for e : lista:
        if(checkingNumber = e):
            count+=1
        else:
            if(count % 2 != 0):
                if(e in primeEratostenes(lista[len(lista)-1]): #Tutaj popraw
                    wynikowa += count * str(e) + " "
            else:
                wynikowa += count * str(e) + " "
            checkingNumber=e
            count=1
    print(lista)
    
def main():
    removePrimeNumber([5,1,7,4,5,6,12,3])
    
main()