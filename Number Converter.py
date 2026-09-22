def convertHex(number): 
    numberFound = False
    i = 1 
    countTotal = 0
    countAmount = 0
    while(numberFound == False): 
        if(number > pow(i, countAmount)): 
            countTotal+=1
        else: 
            

   

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


print("\n\nNow print what number you *want* to have.")
print("1. Binary (Supports only up to two bytes)")
print("2. Hexadecimal")
print("3. Decimal")
num = int(input("Enter (1-3): "))
while (num not in [1,2,3]): 
    print("\nInvalid number!")
    print("Please enter a valud number (1-3):")
    num = int(input("Enter (1-3): "))

print(f"DEBUG: num={num}, original={original}, exit={exit}")

#If the choices are the same, such as decimal to decial
if(original == num): 
    print("\nYour answer is identical: " + str(actualNum))
    exit = True
#You want to go from Binary to Decimal
elif((original == 1 and num == 3) and exit == False): 
    print("\nYour number in decimal format is: " + str(convertDec(actualNum, 1)) + "-DEC")
#You want to go from Hexadecimal to Decimal
elif((original == 2 and num == 3) and exit == False): 
    print("\nYour number in decimal format is: " + str(convertDec(actualNum, 2)) + "-DEC")
#You want to go from binary to hexadecimal
elif((original == 1 and num == 2) and exit == False): 
    dec = convertDec(actualNum, 1)
    
elif(num == 1 and  original == 3 and exit == False): 
    count = False
    result = convertBin(actualNum)
    print("\nYour number in binary is ", end="") 
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
#elif(num == 2 and original == 3 and exit == False): 
#ahh 