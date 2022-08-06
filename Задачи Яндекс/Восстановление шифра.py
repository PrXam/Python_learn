with open("input.txt", "r") as f:
    number_rows = f.readline()
    matrix = []
    for line in f.readlines():
        line.strip()
        matrix.append((line.split(' ')))
    list_num = int(number_rows) * [0]
    for line in matrix:
        index_column = matrix.index(line)
        index_row = 0
        for num in line:
            if int(num) >= 0:
                list_num[index_row] = list_num[index_row] | int(num)
                list_num[index_column] = list_num[index_column] | int(num)
            index_row = index_row+1
list_num = [str(num) for num in list_num]
with open("output.txt", 'w') as f:
    f.write(" ".join(list_num))
