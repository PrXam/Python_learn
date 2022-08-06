def calc(number):
    num_list = [-1, 0]
    for i in range(2, number + 1):
        if i % 2 != 0:
            if i % 3 != 0:
                num_list.append(num_list[i - 1] + 1)
            else:
                num_list.append(min(num_list[i - 1] + 1, num_list[i // 3] + 1))
        else:
            if i % 3 != 0:
                num_list.append(min(num_list[i - 1] + 1, num_list[i // 2] + 1))
            else:
                num_list.append(min(num_list[i - 1] + 1, num_list[i // 3] + 1, num_list[i // 2] + 1))
    return num_list


def recover(num_list):
    operation = num_list[-1]
    index = len(num_list) - 1
    seq = []
    while operation > -1:
        if num_list[index - 1] == operation - 1:
            seq.append(index)
            index -= 1
            operation -= 1
        elif index % 3 == 0:
            seq.append(index)
            index //= 3
            operation -= 1
        else:
            seq.append(index)
            index //= 2
            operation -= 1
    return ' '.join(list(map(str, reversed(seq))))


def main():
    number = int(input())
    num_list = calc(number)
    print(num_list[-1])
    seq = recover(num_list)
    print(seq)


if __name__ == '__main__':
    main()