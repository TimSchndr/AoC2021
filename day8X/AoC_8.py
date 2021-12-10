import numpy as np
from operator import itemgetter

file = open("input8.txt", "r")

input_values = []

display_segments = ["a", "b", "c", "d", "e", "f", "g"]

for line in file:
    input_values.append(line)
    

#tast 1
def getTrivialNumbers(f_input):
    
    total_sum = 0

    for s in f_input:
        a = s.replace("\n", "").split(" | ")[1].split(" ")
    
        for digit in a:
            
            if len(digit) == 2:
                total_sum += 1
                
            elif len(digit) == 3:
                total_sum += 1
            
            elif len(digit) == 4:
                total_sum += 1
            
            elif len(digit) == 7:
                total_sum += 1
    
    return total_sum


def shorterTrivialNumbers(f_input):
    
    y = []
    
    for s in f_input:
        a = s.replace("\n", "").split(" | ")[1].split(" ")
        y.extend(a)
    
    c = [1 for x in y if len(x) in [2, 3, 4, 7]]
    
    return np.sum(np.array(c))


#task 2
def getDecodedSum(f_input):
    
    display_output = 0

    for i in f_input:
        #for every entry line
        
        a = i.replace("\n", "").split(" | ")
        
        #codings
        codings = a[0].split(" ")

        #resulting number
        results = a[1].split(" ")
        
        nontrivial_codes = []
        
        #init codebook
        codebook = {}
        for i in range(1, 10):
            codebook[i] = []
        
        for code in codings:
            
            if len(code) == 2 and codebook[1] == []:
                codebook[1] = list(code)
                    
            elif len(code) == 3 and codebook[7] == []:
                codebook[7] = list(code)

            elif len(code) == 4 and codebook[4] == []: 
                codebook[4] = list(code)
                
            elif len(code) == 7 and codebook[8] == []:
                codebook[8] = list(code)
                
            else:
                nontrivial_codes.append(code)

        for remain in nontrivial_codes:
            
            #distinguish codes of length 6
            #zero is missing here
            #does not work like this
            if len(remain) == 6:
                
                #assume 9
                is_nine = True
                
                for ch in codebook[7]:
                    if not ch in remain:
                        is_nine = False
                        break
                
                if is_nine:
                    codebook[9] = list(remain)
                else:
                    codebook[6] = list(remain)
            
            #distinguish codes of length 5
            if len(remain) == 5:
                
                #get chars that are in 4 but not in one
                four_no_one = []
                
                for ch in codebook[4]:
                    if not ch in codebook[2]:
                        four_no_one.extend(ch)

                #assume 5
                is_five = True                

                for ch in four_no_one:
                    if not ch in remain:
                        is_five = False
                        break
                
                if is_five:
                    codebook[5] = list(remain)
                
                else:
                    
                    #assume 3
                    is_three = True
                    
                    for ch in codebook[1]:
                        if not ch in remain:
                            is_three = False
                    
                    if is_three:
                        codebook[3] = list(remain)
                    else:
                        codebook[2] = list(remain)
                        
        number = ""
            
        for res in results:

            if len(res) == 2:
                number+= "1"
                
            elif len(res) == 3:
                number+= "7"
                
            elif len(res) == 4:
                number += "4"
                
            elif len(res) == 5:
                checks = itemgetter(2, 3, 5)(codebook)
                
                print(checks)
                    
                if checks[0] == sorted(list(res)):
                    number+= "2"
                    
                elif checks[1] == sorted(list(res)):
                    number += "3"
                    
                elif checks[2] == sorted(list(res)):
                    number += "5"
                
            elif len(res) == 6:
                checks = itemgetter(6, 9)(codebook)
                    
                if checks[0] == sorted(list(res)):
                    number += "6"
                else:
                    number += "9"
                    
            elif len(res) == 7:
                number += "8"
            
            print(number)
            print(results)
        
        display_output += int(number)
            
    return display_output

print(f"if-solution {getTrivialNumbers(input_values)}")
print(f"comprehension-solution: {shorterTrivialNumbers(input_values)}")

print(getDecodedSum(input_values))