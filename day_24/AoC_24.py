pos = {"w": 0, "x": 1, "y": 2, "z": 3}
vars = [0, 0, 0, 0]

def read_input(name):

    file = open(name)
    instr = []

    for line in file:
        line = line.strip().split(" ")

        instr.append(line)

    return instr

def get_values(op):

    if op[2].isdigit():
        return pos[op[1]], op[2]
    else:
        return pos[op[1]], vars[pos[op[2]]]

def calculate(op_set, input):

    for op in op_set:

        if op[0] == "inp":
            vars[pos(op[1])] = input
        else:
            a, b = get_values(op)
            if op[0] == "add":
                vars[a] = vars[a] + b
            elif op[0] == "mul":
                vars[a] = vars[a] * b
            elif op[0] == "div":
                vars[a] = int(vars[a] / b)
            elif op[0] == "mod":
                vars[a] = vars[a] % b
            elif op[0] == "eql":
                vars[a] = 1 if vars[a] == b else 0

if __name__ == "__main__":

    instr = read_input("input24.txt")