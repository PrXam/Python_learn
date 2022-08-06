def lis_bottom_up(arr, number):
    max_seq_arr = []
    for i in range(number):
        max_seq_arr.append(1)
        for j in range(i):
            if arr[i] <= arr[j] and max_seq_arr[j] + 1 > max_seq_arr[i]:
                max_seq_arr[i] = max_seq_arr[j] + 1
    index = 0
    for i in range(len(max_seq_arr)):
        if max_seq_arr[i] > max_seq_arr[index]:
            index = i
    return index, max_seq_arr


def recieve_ans(arr, max_seq_arr, index):
    max_seq = [0 for i in range(max_seq_arr[index])]
    cur_elem = index
    j = max_seq_arr[index] - 1
    while cur_elem > -1:
        if max_seq_arr[cur_elem] == max_seq_arr[index] - 1 and arr[cur_elem] >= arr[index]:
            max_seq[j] = str(index + 1)
            j -= 1
            index = cur_elem
        else:
            cur_elem -= 1
    max_seq[0] = str(index + 1)
    return ' '.join(max_seq)


def main():
    number = int(input())
    arr = list(map(int, input().split()))
    index, max_seq_arr = lis_bottom_up(arr, number)
    max_seq = recieve_ans(arr, max_seq_arr, index)
    print(max_seq_arr[index])
    print(max_seq)


if __name__ == '__main__':
    main()
