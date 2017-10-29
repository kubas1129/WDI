import math

def toDec(base, value):
    count = 1
    decimal = 0
    for i in str(value):
        if(i >= "A" and i <= "Z"):
            switcher = {
                "A":10,
                "B":11,
                "C":12,
                "D":13,
                "E":14,
                "F":15
            }
            decimal += switcher.get(i, 0) * int(math.pow(base, len(str(value)) - count))
        else:
            decimal += int(i) * int(math.pow(base, len(str(value)) - count))
        count += 1
    return decimal


def fromDec(base, value):
    output = ""
    while(value != 0):
        print(value)
        if(value % base <= 9):
            output += str(value % base)
        else:
            switcher = {
                10: "A",
                11: "B",
                12: "C",
                13: "D",
                14: "E",
                15: "F"
            }
            output += switcher.get(value % base, "N")
        value = int(value / base)
    return output[::-1]





def main():
    print(toDec(16, "AB"))
    #print(fromDec(16,699))

main()