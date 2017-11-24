# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 08:25:03 2017

@author: palkjaku
"""

import math
import time


def NumericError():
    x = 1.123456789*10e14
    result1 = x + 0.1 - x
    result2 = x - x + 0.1
    return {result1,result2}
    
    
def loopFor(x, count):
    suma = 0    
    for i in range(count):
        suma += 0.3
    return suma
    
    
def XYCalc(x,y):
    if(x == 0):
        return "ox"
    elif(y == 0):
        return "oy"
    else:       
        q = math.degrees(math.atan2(y,x))
        if(q > 0):
            return math.floor(q/90 + 1)
        else:
            return math.floor((360+q)/90 + 1)
    

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

    
    

def main():
    #print(NumericError())
    
    #print(loopFor(0.3,3000))
    
    #print(XYCalc(-1,4))

    ll = primeEratostenes(1000)
    print(ll)
    
main()