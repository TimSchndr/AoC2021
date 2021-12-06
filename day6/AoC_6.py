import numpy as np

file = open("input6.txt", "r")

input_values = []

for line in file:
    input_values = (line.split(","))

def count_fish(starting_fish, days):
    
    curr_counts = np.zeros(9)
    
    for s in starting_fish:
        curr_counts[int(s)] += 1
        
    #starting number of fish
    number_of_fish = sum(curr_counts)
    
    for day in range(days):
        
        new_counts = np.zeros(9)
        
        #new baby fish
        new_counts[8] = curr_counts[0]
        number_of_fish += curr_counts[0]
        
        new_counts[6] = curr_counts[0] + curr_counts[7]
        new_counts[7] = curr_counts[8]
        
        for i in range(6):
            new_counts[i] = curr_counts[i+1]        
        
        curr_counts = new_counts
    
    return number_of_fish

print(int(count_fish(input_values, 80)))
print(int(count_fish(input_values, 256)))