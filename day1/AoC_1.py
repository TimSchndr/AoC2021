file = open("C://Users//timsc//Desktop//input1.txt", "r")

input_values = []

for line in file:
    input_values.append(int(line))



def tallerThanPredecessor(f_input):
    
    counter = 0
    
    for i in range(1, len(input_values)):
        if (input_values[i] - input_values[i-1]) > 0:
            counter += 1

    return counter

def threeSlidingWindow(f_input):
    
    counter = 0
    
    threeSum = []
    
    for i in range(0, len(input_values)-2):
        threeSum.append(sum(input_values[i:i+3]))
    
    for i in range(1, len(threeSum)):
        if threeSum[i] - threeSum[i-1] > 0:
            counter+= 1    
    
    return counter