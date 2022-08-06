def edit_distance(matrix, first_word, second_word):
    for i in range(1, len(first_word) + 1):
        matrix.append([i])
        for j in range(1, len(second_word) + 1):
            diff = int(first_word[i - 1] != second_word[j - 1])
            matrix[i].append(min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + diff))
    return matrix[-1][-1]


def main():
    first_word = input()
    second_word = input()
    matrix = [[i for i in range(len(second_word) + 1)]]
    num = edit_distance(matrix, first_word, second_word)
    print(num)


if __name__ == '__main__':
    main()
