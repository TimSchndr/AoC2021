def convert_char(char):
    if char in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
           #in [str(x) for x in list(range(0, 10))]:
        return format(ord(char), '08b')[4:]
    else:
        if char=='A':
            return "1010"
        elif char == 'B':
            return "1011"
        elif char == 'C':
            return "1100"
        elif char == 'D':
            return "1101"
        elif char == 'E':
            return "1110"
        elif char == 'F':
            return "1111"

def read_package(start, bin_string):

    if bin_string[start+3:start+6] == "100":
        # number package

        # format:   [version, ID, number]
        pkg_info = [bin_string[start:start+3], bin_string[start+3:start+6]]

        index = start+6
        number = ""

        while bin_string[index] == "1":
            print(index)
            number += bin_string[index+1:index+5]
            index += 5

        # add the last four digits
        number += bin_string[index+1:index+5]

        #calculate number of trailing zeros, correct index
        if (index - start)%16 != 0:
            index += (index - start)%16

        pkg_info.append(int(number, 2))

        return pkg_info, index

    else:
        # operator package

        return

def task_1(bin_str):
    return

if __name__ == '__main__':

    file = open("input16.txt", "r")
    input_values = file.readline().replace('\n', '')
    file.close()

    bin_str = ""
    for c in input_values:
        bin_str += convert_char(c)

    #print(int("011111100101", 2))
    print(read_package(0, "110100101111111000101000"))
