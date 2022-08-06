def lis_bottom_up(arr, number):
    max_seq_arr = []
    for i in range(number):
        max_seq_arr.append(1)
        for j in range(i):
            if arr[i] % arr[j] == 0 and max_seq_arr[j] + 1 > max_seq_arr[i]:
                max_seq_arr[i] = max_seq_arr[j] + 1
    return max(max_seq_arr)


def main():
    number = int(input())
    arr = list(map(int, input().split()))
    max_seq = lis_bottom_up(arr, number)
    print(max_seq)


if __name__ == '__main__':
    main()
