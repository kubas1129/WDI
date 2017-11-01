# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 08:24:49 2017

@author: palkjaku
"""

import time

def silniaRek(x):
    if(x < 0):
        print("Argument nie moze byc ujemny")
        return
    if(x == 0):
        return 1 
    else:
        x *= silniaRek(x-1)
    return x
    
def silniaIter(x):
    if(x < 0):
        print("Argument nie moze byc ujemny")
        return
    if(x == 0):
        print("1")
        return 1    
    wynik = 1
    for i in range(x):
        wynik *= (i+1)
    return wynik
    

def fibonacciRek(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
       return fibonacciRek(n-1) + fibonacciRek(n-2)


def fibonacciIter(n):
    fib = 0
    f1 = 0
    f2 = 1
    for i in range(n-1):
        if(n == 0):
            return 0
        elif(n == 1):
            return 1
        else:
            fib = f1 + f2
            f1 = f2
            f2 = fib
    return fib

def dwumianNewtona(n,k):
    return int(silniaIter(n)/(silniaIter(k) * silniaIter(n-k)))
    

def pascalTriangle(n):
    if(n < 0):
        return
    elif(n <= 1):
        pascalTriangle(n-1)
        print((n + 1) * "1 ")
        return
    else:
        pascalTriangle(n - 1)
        print("1 ", end='')
        for i in range(n-1):
            print(str(dwumianNewtona(n,i+1)) + " ", end='')
        print("1", end='')
        print()
        return
        
    
def main():
    start = time.time()
    silniaRek(5)
    end = time.time()
    print("Rekurencjyjny czas: " + str(end - start))    
    
    start = time.time()
    silniaIter(5)
    end = time.time()
    print("Iteracyjny czas: " + str(end - start))    
    
    print("FibRek: " + str(fibonacciRek(6)))
    print("FibIter: " + str(fibonacciIter(4)))

    pascalTriangle(6)

main()