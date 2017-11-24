#Jakub Pałka

import matplotlib.pyplot as plt
import time

def primeEratostenes(n):
    if (n < 2): return -1
    primes = [i+1 for i in range(n)]  #init tablicy liczb
    primes.remove(1)  #usuwamy 1
    j = 0  #counter while
    start_time =  time.time()
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
    fun_time = time.time()-start_time
    return primes, fun_time


#Główne ciało programu
def main():
    timeList = []

    out = primeEratostenes(10)
    timeList.append(out[1])

    out = primeEratostenes(100)
    timeList.append(out[1])

    out = primeEratostenes(500)
    timeList.append(out[1])

    out = primeEratostenes(1000)
    timeList.append(out[1])

    out = primeEratostenes(5000)
    timeList.append(out[1])

    out = primeEratostenes(10000)
    timeList.append(out[1])

    out = primeEratostenes(20000)
    timeList.append(out[1])

    out = primeEratostenes(40000)
    timeList.append(out[1])

    out = primeEratostenes(60000)
    timeList.append(out[1])

    #Rysowanie wykresu
    plt.plot([10,100,500,1000,5000,10000,20000, 40000,60000],timeList,'ro')
    plt.xlabel('Primes Range')
    plt.ylabel('Time (s)')
    plt.axis([0, 60000, 0, 60])
    plt.show()


main()