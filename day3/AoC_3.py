import math

file = open("input3.txt", "r")

input_strings = []
input_numbers = []

for line in file:
    input_strings.append(line.replace("\n", ""))
    input_numbers.append((int(line, base=2)))
    

def getPowerConsumption(f_input):
    
    numberOfBits = math.floor(math.log(max(f_input), 2)) + 1
    
    gamma_rate = 0
    epsilon_rate = 0
    
    for i in range(0, numberOfBits):
        #for each bit
        
        checkNum = 1 << i
        
        #counter for bit state
        zeros = 0
        ones = 0
        
        for j in f_input:
            #for each number in the input
            
            if(j & checkNum):
                ones += 1
            else:
                zeros += 1
        
        if zeros < ones:
            #most common bit is 1
            gamma_rate += (1 << i)
            epsilon_rate += (0 << i)
        
        else:
            #most common bit is 0
            gamma_rate += (0 << i)
            epsilon_rate += (1 << i)
    
    return gamma_rate * epsilon_rate


def getLifeSupportRating(f_input):
    
    oxyL = f_input.copy()
    pos = 0
    
    while(len(oxyL) > 1):
        zeros = 0
        ones = 0
        
        for number in oxyL:
            if number[pos] == '1':
                ones+= 1
            else:
                zeros+= 1
            
        char = "a"    
        if ones > zeros:
            char = '1'
        elif ones == zeros:
            char = '1'
        else:
            char = '0'
        
        numberToDelete = []
        
        for number in oxyL:
            if number[pos] != char:
                numberToDelete.append(number)
        
        for element in numberToDelete:
            oxyL.remove(element)
        
        pos+=1
        
        
    # the same for carbon
    
    carbL = f_input.copy()
    pos = 0
    
    while(len(carbL) > 1):
        zeros = 0
        ones = 0
        
        for number in carbL:
            if number[pos] == '1':
                ones+= 1
            else:
                zeros+= 1
            
        char = "a"    
        if ones > zeros:
            char = '0'
        elif ones == zeros:
            char = '0'
        elif ones < zeros:
            char = '1'
        
        x = []
        
        for number in carbL:
            if number[pos] != char:
                x.append(number)
        
        for q in x:
            carbL.remove(q)

        pos+=1
    
    return int(carbL[0], 2) * int(oxyL[0], 2)


print(getPowerConsumption(input_numbers))
print(getLifeSupportRating(input_strings))
