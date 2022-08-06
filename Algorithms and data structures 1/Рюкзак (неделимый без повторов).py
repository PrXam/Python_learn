def knapsack(weight, num, list_gold):
    matrix = [[0 for i in range(weight + 1)]]
    for i in range(1, num + 1):
        matrix.append([0])
        for w in range(1, weight + 1):
            matrix[i].append(matrix[i - 1][w])
            if list_gold[i - 1] <= w:
                matrix[i][w] = max(matrix[i][w], matrix[i - 1][w - list_gold[i - 1]] + list_gold[i - 1])
    return matrix[-1][-1]


def main():
    weight, num, = input().split()
    weight = int(weight)
    num = int(num)
    list_gold = list(map(int, input().split()))
    max_weight = knapsack(weight, num, list_gold)
    print(max_weight)


if __name__ == '__main__':
    main()
