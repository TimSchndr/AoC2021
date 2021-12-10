import numpy as np

file = open("input4.txt", "r")

#read first line, transform to int list
numbers = list(map(int, file.readline().split(',')))

gameboards = []
current_board = np.array([])

line_counter = 0

for line in file:
    if line.startswith('\n'):
        continue
    else:
        if line.startswith(" "):
            line = line.replace(' ', '', 1)
        
        line = line.replace('  ', ' ')
        line = line.replace('\n', '').split(' ')
        
        #transform strings to ints
        line = list(map(int, line))        
        
        #create a new row of the current board and apend it
        board_row = np.array(line)
        current_board = np.r_[current_board, board_row]
        
        line_counter += 1
        
        if(line_counter > 4):
            #the board is full (5x5), append it to board list, continue with next board
            gameboards.append(current_board.reshape((5, 5)))
            current_board = np.array([])
            line_counter = 0


def findWinningBoard(f_numbers, f_gameboards):
    
    #track the number of changes in each board
    change_counter = np.zeros(len(f_gameboards))
    
    for number in f_numbers:
        #iterate over each number
        
        for idx, board in enumerate(f_gameboards):
            if number in board:
                #position of number in board
                position = np.argwhere(board == number)[0]

                #replace number with a value not present in any board
                board[position[0],position[1]] = -1
                
                #add a change for the board
                change_counter[idx] += 1

                if (np.all(board[position[0], :] == -1) or np.all(board[:, position[1]] == -1)):
                    #the change made the board winning
                    
                    #add up the numbers in the board, correct '-1' for all changed numbers
                    return (np.sum(board) + change_counter[idx]) * number

def findLastWinningBoard(f_numbers, f_gameboards):
    
    #track the number of changes in each board
    change_counter = np.zeros(len(f_gameboards))
    
    #track all finished boards with bool: 0 or 1
    completed_boards = np.zeros(len(f_gameboards))
    
    #index of number that makes penultimate board win
    num_index_break = None
        
    for n_idx, number in enumerate(f_numbers):
            
        for idx, board in enumerate(f_gameboards):
            
            #check if board has been completed
            if number in board and not completed_boards[idx]:
                
                #find position of number, change it, notice change
                position = np.argwhere(board == number)[0]
                board[position[0],position[1]] = -1
                        
                change_counter[idx] += 1
                        
                if (np.all(board[position[0], :] == -1) or np.all(board[:, position[1]] == -1)):
                    #notice that the board won
                    completed_boards[idx] = 1
                
        #check if only one board is left
        if np.sum(completed_boards) == len(f_gameboards)-1:
            #notice index of current number
            num_index_break = n_idx
            break
    
    #play last board to end
    for number in f_numbers[num_index_break:]:
        
        for idx, board in enumerate(f_gameboards):
            if number in board and not completed_boards[idx]:
                position = np.argwhere(board == number)[0]
    
                board[position[0],position[1]] = -1
                        
                change_counter[idx] += 1
                        
                #the kast board wins
                if (np.all(board[position[0], :] == -1) or np.all(board[:, position[1]] == -1)):
                    return (np.sum(board) + change_counter[idx]) * number
    

print(f"Result for Winning Board: {findWinningBoard(numbers, gameboards)}.")
print(f"Result for Last Winning Board: {findLastWinningBoard(numbers, gameboards)}.")
