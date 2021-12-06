import numpy as np

file = open("input5.txt", "r")

input_values = []
max_coord = 0

for line in file:
    slope = line.split(" -> ")
    
    x1, y1 = map(int, slope[0].split(","))
    x2, y2 = map(int, slope[1].split(","))
    
    #the max coord to determine size of array
    if max_coord < max(x1, x2, y1, y2):
        max_coord = max(x1, x2, y1, y2)
    
    input_values.append([[x1, y1], [x2, y2]])

def findOverlappingOrthoLines(vent_lines, dims):
    
    seabed = np.zeros((dims, dims))
    
    for line in vent_lines:
        
        #check if line is vertical
        if line[0][0] == line[1][0]:

            #get length of line
            length = abs(line[0][1] - line[1][1]) + 1
            
            x = line[0][0]
            y_start = min(line[0][1], line[1][1])
            
            for i in range(0, length):
                seabed[x][y_start+i] += 1
            
        
        #check if line is horizontal
        elif line[0][1] == line[1][1]:
            length = abs(line[0][0] - line[1][0]) +1
            
            x_start = min(line[0][0], line[1][0])
            y = line[0][1]
            
            for i in range(0, length):
                seabed[x_start+i][y] += 1
    
    return np.sum(seabed >1)

'''
Would be nicer if I used the above method again!
'''
def findOverlappingLines(vent_lines, dims):
    
    seabed = np.zeros((dims, dims))
    
    for line in vent_lines:
        
        #check if line is vertical
        if line[0][0] == line[1][0]:

            #get length of line
            length = abs(line[0][1] - line[1][1]) + 1
            
            x = line[0][0]
            y_start = min(line[0][1], line[1][1])
            
            for i in range(0, length):
                seabed[x][y_start+i] += 1
        
        #check if line is horizontal
        elif line[0][1] == line[1][1]:
            length = abs(line[0][0] - line[1][0]) +1
            
            x_start = min(line[0][0], line[1][0])
            y = line[0][1]
            
            for i in range(0, length):
                seabed[x_start+i][y] += 1
        
        #check if line has angle of 45 degrees
        elif abs(line[0][0] - line[0][1]) == abs(line[1][0] - line[1][1]):

            length = abs(line[0][0] - line[1][0]) + 1
            
            #determine direction            
            if (line[0][0] - line[0][1]) == 0:
                direction = 1
                x_start = min(line[0][0], line[1][0])
                y_start = min(line[0][1], line[1][1])
                
            else:
                direction = -1
                x_start = min(line[0][0], line[1][0])
                y_start = max(line[0][1], line[1][1])
            
            for i in range(length+1):
                
                seabed[x_start+i][y_start+(direction*i)] += 1
            
    return np.sum(seabed >1)
    

print(findOverlappingOrthoLines(input_values, max_coord))
print(findOverlappingLines(input_values, max_coord))