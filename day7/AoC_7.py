import numpy as np

file = open("input7.txt", "r")

input_values = []

for line in file:
    input_values.append(list(map(int, line.split(","))))

#task one
numbers = np.array(input_values[0])
median = np.median(input_values)

print(np.sum(abs(numbers-median)))

#second task
distances = []

for i in range(0, 1000):
    x = 0
    
    for n in numbers:
        x+= abs(n-i) * (abs(n-i)+1)
    
    distances.append(x/2)

print(np.min(distances))
