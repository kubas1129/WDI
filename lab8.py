import random


def initTable(size):
    return [random.randint(0,100) for i in range(size)]

def sortByChoosed(numbers):
    for i in range(len(numbers)):
        minimum=i
        for j in range(i,len(numbers)):
            if(numbers[j] < numbers[minimum]):
                minimum=j
        numbers[i],numbers[minimum]=numbers[minimum],numbers[i]
    return numbers


def sortByInsert(numbers):
    sort = []
    sort.append(numbers[-1])
    for e in range(len(numbers)-2,-1,-1):
        for i in range(len(sort)):
           if(numbers[e] <= sort[i]):
               sort.insert(i,numbers[e])
               break
           elif(i == len(sort)-1):
               sort.append(numbers[e])

    return sort


def bubbleSort(numbers):
    for k in numbers:
        for i in range(len(numbers)-1):
            if(numbers[i] > numbers[i+1]):
                numbers[i],numbers[i+1]=numbers[i+1],numbers[i]
    return numbers



def divide(s,k,lista):
    p = k #ostatni element z ktorym porownujemy dana liste
    i=0
    j=0
    for e in range(k+1):
        if(lista[i] < lista[p]):
            lista[i],lista[j]=lista[j],lista[i]
            j += 1
        i += 1
    lista[p],lista[j]=lista[j],lista[p]
    return j

def quickSort(s,k,lista):
    pivot = divide(s,k,lista)
    if(pivot == k):
        return lista
    quickSort(s,pivot,lista)
    quickSort(pivot+1,k,lista)
    return lista



def main():
    toSort = [1,5,8,7,15,4,3]
    #print(sortByChoosed(initTable(100)))
    #print(sortByInsert([100,20,1,87,76,2,9,34,22]))
    #print(bubbleSort(initTable(100)))
    print(quickSort(0,len(toSort)-1,toSort))

main()