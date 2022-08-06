import sys


def binary_search(num, num_list1):
    beg = 0
    end = len(num_list1) - 1
    while beg <= end:
        index = int(beg + (end - beg)/2)
        if num_list1[index] == num:
            return str(index + 1)
        elif int(num_list1[index]) > int(num):
            end = index - 1
        else:
            beg = index + 1
    return '-1'


def main():
    line1 = sys.stdin.readline()
    n, str_list1 = line1.split(' ', 1)
    num_list1 = str_list1.split()
    line2 = sys.stdin.readline()
    k, str_list2 = line2.split(' ', 1)
    num_list2 = str_list2.split()
    resolve = []
    for num in num_list2:
        resolve.append(binary_search(num, num_list1))
    print(" ".join(resolve))


if __name__ == "__main__":
    main()