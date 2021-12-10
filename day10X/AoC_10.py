import numpy as np
from collections import deque

file = open("input10.txt", "r")

data = []

for line in file:
    data.append(line.replace("\n", ""))


#test data
#a = ["[({(<(())[]>[[{[]{<()<>>", "[(()[<>])]({[<{<<[]>>", "(((({<>}<{<{<>}{[]{[]{", "{<[[]]>}<{[{[{[]{()[[[]", "<{([{{}}[<[[[<>{}]]]>[]]"]


opener = {"(": 1, "[": 2, "{": 3, "<": 4}
closer = {")": 1, "]": 2, "}": 3, ">": 4}
rev_closer = {1: ")", 2: "]", 3: "}", 4: ">" }

def getSyntaxErrorScore(f_input):
    
    counter = np.zeros(4)
    scores = np.array([3, 57, 1197, 25137])
    
    stack = deque()
    
    for line in f_input:
        
        for char in line:
            #check every index
           
            if char in opener:
                #opening symbol
                stack.append(char)
            else:
               #closing symbol, check if correct
               
               if stack:
                   #not empty
                   sym = stack.pop()
                   if not opener[sym] == closer[char]:
                       counter[closer[char]] += 1
                       break
               else:
                   break
    
    return np.sum(counter*scores)

def repairCode(f_input):
    
    stack = deque()
    correction = []   
    for idx, line in enumerate(f_input):
        corrupt = False
        
        for char in line:
            
            if char in opener:
                #opening symbol
                stack.append(char)
            
            else:
                #closing symbol, checkif correct
                
                if stack:
                    #not empty
                    sym = stack.pop()
                    
                    if not opener[sym] == closer[char]:
                        #the line is corrupted
                        corrupt = True
                        break
        
        missing_chars = []
        while stack and not corrupt:
            #still chars in stack, but line is correct
            sym = stack.pop()
            
            missing_chars.extend(rev_closer[opener[sym]])
        
        if len(missing_chars) > 0:
            correction.append(missing_chars)
    
    scores = []
    for ext in correction:
        score = 0
        for c in ext:
            score *= 5
            score += closer[c]
        
        scores.append(score)
    
    #return np.median(np.array(scores))
    

#print(getSyntaxErrorScore(data))
print(repairCode(data))