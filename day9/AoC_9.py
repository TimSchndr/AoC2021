import numpy as np

file = open("input9.txt", "r")

matrix = []
rows = columns = 0


f_line = file.readline().replace("\n", "")
columns = len(list(f_line))
rows += 1

matrix.extend(list(map(int, list(f_line))))

for line in file:
    
    line = line.replace("\n", "")
    
    rows += 1
    matrix.extend(list(map(int, list(line))))

data = np.array(matrix).reshape((rows, columns))

    




