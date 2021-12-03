file = open("input2.txt", "r")

input_values = []

for line in file:
    input_values.append(line)

def getFinalPosition(f_input):
    
    depth = 0
    position = 0
    
    for value in f_input:
        x = value.split()
        
        
        if x[0] == "forward":
            position += int(x[1])
        elif x[0] == "down":
            depth += int(x[1])
        elif x[0] == "up":
            depth -= int(x[1])
        
    return depth * position

def getFinalPosition_new(f_input):
    
    depth = 0
    position = 0
    aim = 0
    
    for value in f_input:
        x = value.split()
        
        if x[0] == "forward":
            position += int(x[1])
            depth += aim * int(x[1])
        elif x[0] == "down":
            aim += int(x[1])
        elif x[0] == "up":
            aim -= int(x[1])
        
    return depth * position


print(getFinalPosition_new(input_values))
