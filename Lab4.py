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
    #print(x)
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
        #print(wynik)
        wynik *= (i+2)
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
    for i in range(n):
        if(n == 0):
            return 0
        elif(n == 1):
            return 1
        else:
            fib = f1 + f2
            f1 = f2
            f2=fib
    return fib
    
    
        
    
def main():
    start = time.time()
    silniaRek(5)
    end = time.time()
    print("Rekurencjyjny czas: " + str(end - start))    
    
    start = time.time()
    silniaIter(5)
    end = time.time()
    print("Iteracyjny czas: " + str(end - start))    
    
    print("FibRek: " + str(fibonacciRek(4)))
    print("FibIter: " + str(fibonacciIter(2)))
    
main()