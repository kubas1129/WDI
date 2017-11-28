# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 08:41:57 2017

@author: palkjaku
"""

ceny = {1:1,2:3}

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

    

def removePrimeNumber(lista):
    lista.sort()
    checkingNumber=lista[0]
    count=0
    wynikowa = ""
    primes = primeEratostenes(lista[len(lista)-1])
    for i in range(len(lista)):
        if(checkingNumber == lista[i]):
            count += 1
        else:
            if(count % 2 != 0):
                if (not(checkingNumber in primes)):
                    wynikowa += count * (str(checkingNumber) + " ")
            else:
                wynikowa += count * (str(checkingNumber) + " ")
            checkingNumber = lista[i]
            count = 1
        if(i == len(lista)-1):
            if (count % 2 != 0):
                if (not (checkingNumber in primeEratostenes(lista[len(lista) - 1]))):
                    wynikowa += count * (str(checkingNumber) + " ")
            else:
                wynikowa += count * (str(checkingNumber) + " ")

    return wynikowa





def main():
    print(removePrimeNumber([5,7,4,18,3,7,5,1,2,12,7,13]))
    
main()