def count_num(number_list, num_count):
    for num in number_list:
        num_count[num] += 1
    for i in range(1, 11):
        num_count[i] += num_count[i-1]


def sorting(number_list, num_count, num):
    sort_list = [0 for i in range(num)]
    for i in range(num - 1, -1, -1):
        sort_list[num_count[number_list[i]] - 1] = number_list[i]
        num_count[number_list[i]] -= 1
    return sort_list


def main():
    num = int(input())
    number_list = list(map(int, input().split()))
    num_count = [0 for i in range(11)]
    count_num(number_list, num_count)
    sort_list = sorting(number_list, num_count, num)
    print(' '.join(map(str, sort_list)))


if __name__ == '__main__':
    main()