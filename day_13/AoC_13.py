import numpy as np

def read_input(filename):

    pairs = []
    folds = []
    file = open(filename)

    for line in file:
        #line.replace("\n", "")
        if line[0].isdigit():
            x, y = line.strip().split(",")
            pairs.append([int(x), int(y)])

        elif line[0] == '\n':
            continue

        else:
            axis, koord = line.strip().replace("fold along ", "").split("=")
            folds.append([axis, int(koord)])

    file.close()
    return pairs, folds

def init_sheet(points):

    sheet = np.zeros((max([x[1] for x in points])+1, max([x[0] for x in points])+1))

    for point in points:
        sheet[point[1], point[0]] = 1

    return sheet

def fold_sheet(sheet, instr):

    if instr[0] == "y":
        if sheet.shape[0] %2 == 0:
            new_sheet = sheet[0:instr[1], :] + np.flipud(sheet[instr[1]:, :])
        else:
            new_sheet = sheet[0:instr[1], :] + np.flipud(sheet[instr[1]+1:, :])

    else:
        if sheet.shape[1] % 2 == 0:
            new_sheet = sheet[:, 0:instr[1]] + np.fliplr(sheet[:, instr[1]:])
        else:
            new_sheet = sheet[:, 0:instr[1]] + np.fliplr(sheet[:, instr[1]+1:])

    return new_sheet>0

def print_sheet(sheet):
    for line in sheet:
        s = ""
        for p in line:
            if p == 1:
                s+= "#"
            else:
                s+= "."

        print(s)

if __name__ == "__main__":
    points, folds = read_input("input13.txt")

    sheet = init_sheet(points)

    # task1
    print(np.sum(fold_sheet(sheet, folds[0])))

    # task2
    for fold in folds[:]:

        sheet = fold_sheet(sheet, fold)

    print_sheet(sheet)
