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


def main():
    #print(sortByChoosed(initTable(100)))
    #print(sortByInsert([100,20,1,87,76,2,9,34,22]))
    #print(bubbleSort(initTable(100)))

main()