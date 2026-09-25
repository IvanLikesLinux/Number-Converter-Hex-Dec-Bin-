def convertHex(number):
    result = "" 
    tempResult = 0
    numberFound = False
    countTotal = 0
    while(numberFound == False): 
        if(number > 15*pow(16, countTotal+1)): 
            countTotal+=1
        else: 
            numberFound = True
    for i in range(countTotal, -1, -1):
        temporary = 15
        while(temporary * pow(16,i) > number ):
            temporary-=1
        tempResult =  temporary
        number-=tempResult * pow(16,i)
        if(tempResult == 10): 
            result+="A"
        elif(tempResult == 11): 
            result+="B"
        elif(tempResult == 12): 
            result+="C"
        elif(tempResult == 13): 
            result+="D"
        elif(tempResult == 14): 
            result+="E"
        elif(tempResult == 15): 
            result+="F"
        else: 
            result+=str(tempResult)
    return result 
   

def convertDec(number, type): 
    if(type == 1): 
        digitList = [int(d) for d in str(number)]
        size = len(digitList)
        totalNum = 0
        for i in range(size-1,-1,-1): 
            if(digitList[i] == 1): 
                totalNum+=pow(2, size-1-i)
        return totalNum
    elif(type == 2):
        digitList = list(number)
        for i in range (0,len(digitList),1): 
            if(digitList[i] == "a" or digitList[i] == "A"): 
                digitList[i] = 10
            elif(digitList[i] == "b" or digitList[i] == "B"): 
                digitList[i] = 11
            elif(digitList[i] == "c" or digitList[i] == "C"): 
                digitList[i] = 12
            elif(digitList[i] == "d" or digitList[i] == "D"): 
                digitList[i] = 13
            elif(digitList[i] == "e" or digitList[i] == "E"): 
                digitList[i] = 14
            elif(digitList[i] == "f" or digitList[i] == "F"): 
                digitList[i] = 15
        digitList = [int(d) for d in digitList]
        size = len(digitList)
        totalNum = 0
        for i in range(size-1,-1,-1): 
            totalNum+=digitList[i] * pow(16, size-1-i)
        return totalNum




binaryValues = [65536,32768,16384,8192,4096,2048,1024,512,256,128,64,32,16,8,4,2,1]
binaryList = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] #17 PHYSICAL bits 
def convertBin(number):
    if(number >= 131072):
        print("That number is too big for this program, we can only accept numbers up to two bytes and 1 bite (17 bits)")
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range (0,17,1):
        if(number >= binaryValues[i]): 
            binaryList[i] = 1
            number-=binaryValues[i]
    return binaryList

print("Welcome to number converter, please select what number you have.") 
print("1. Binary")
print("2. Hexadecimal")
print("3. Decimal")
exit = False
original = int(input("Enter (1-3): "))
while (original not in [1,2,3]): 
    print("\nInvalid number!")
    print("Please enter a valud number (1-3):")
    original = int(input("Enter (1-3): "))
if (original == 1 or original == 3):
    actualNum = int(input("Enter the actual number(Z): "))
else: 
    actualNum = input("Enter the actual number(R): ")

print("\n", end="")
for i in range(0,10,1):
    print("-",end="")
print("")
if(original == 1): 
    print("Decimal: " + str(convertDec(actualNum,1)) + "-DEC")
elif (original == 3): 
    print("Decimal: " + str(actualNum) + "-DEC")
else: 
    print("Decimal: " + str(convertDec(actualNum,2)) + "-DEC")
if(original == 1): 
    dec = convertDec(actualNum, 1)
    print("Hexadecimal: " + str(convertHex(dec)) + "-HEX")
elif (original == 2): 
    print("Hexadecimal: " + str(actualNum) + "-HEX")
else: 
    print("Hexadecimal: " + str(convertHex(actualNum)) + "-HEX")
if(original == 1): 
    print("Binary: " + str(actualNum) + "-BIN")
elif (original == 2): 
    dec = convertDec(actualNum, 2)
    count = False
    result = convertBin(dec)
    print("Binary: ", end="") 
    zeroCount = 0
    for i in range(0,17,1): 
        if(result[i] != 1 and count == False):
            zeroCount+=1
            continue
        else: 
            count = True
        print(result[i], end="")
    if(zeroCount == 17): 
        print("0", end="")
    print("-BIN")
else: 
    count = False
    result = convertBin(actualNum)
    print("Binary: ", end="") 
    zeroCount = 0
    for i in range(0,17,1): 
        if(result[i] != 1 and count == False):
            zeroCount+=1
            continue
        else: 
            count = True
        print(result[i], end="")
    if(zeroCount == 17): 
        print("0", end="")
    print("-BIN")
print("\n", end="")
for i in range(0,10,1):
    print("-",end="")
print()


if original == 1:
    print("Decimal: " + str(int(str(actualNum), 2)) + "-DEC")
elif original == 3:
    print("Decimal: " + str(actualNum) + "-DEC")
else:
    print("Decimal: " + str(int(actualNum, 16)) + "-DEC")

if original == 1:
    print("Hexadecimal: " + hex(int(str(actualNum), 2))[2:].upper() + "-HEX")
elif original == 2:
    print("Hexadecimal: " + str(actualNum) + "-HEX")
else:
    print("Hexadecimal: " + hex(actualNum)[2:].upper() + "-HEX")

if original == 1:
    print("Binary: " + str(actualNum) + "-BIN")
elif original == 2:
    print("Binary: " + bin(int(actualNum, 16))[2:] + "-BIN")
else:
    print("Binary: " + bin(actualNum)[2:] + "-BIN")