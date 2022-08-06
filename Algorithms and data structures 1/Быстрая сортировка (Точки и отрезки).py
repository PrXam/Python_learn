import sys
import math
import random


def partition(arr, left, right):
    index = random.randint(left, right - 1)
    arr[left], arr[index] = arr[index], arr[left]
    x = arr[left]
    ml = 0
    mr = left
    for i in range(left + 1, right + 1):
        if arr[i] < x:
            mr += 1
            arr[mr], arr[i] = arr[i], arr[mr]
        elif arr[i] == x:
            mr += 1
            ml += 1
            arr[left + ml], arr[i] = arr[i], arr[left + ml]
            if left + ml != mr:
                arr[mr], arr[i] = arr[i], arr[mr]
    for i in range(ml + 1):
        arr[left + i], arr[mr - i] = arr[mr - i],  arr[left + i]
    ml = mr - ml
    return ml, mr


def quicksort(arr, left, right):
    if left >= right:
        return 0
    ml, mr = partition(arr, left, right)
    quicksort(arr, left, ml - 1)
    quicksort(arr, mr + 1, right)


def binary_search_beg(dot, arr):
    beg = 0
    end = len(arr) - 1
    res = -1
    while beg <= end:
        middle = (beg + end) / 2
        middle = math.ceil(middle)
        if dot < arr[middle]:
            end = middle - 1
        else:
            res = middle
            beg = middle + 1
    return res + 1


def binary_search_end(dot, arr):
    beg = 0
    end = len(arr) - 1
    res = -1
    while beg <= end:
        middle = (beg + end) / 2
        middle = math.ceil(middle)
        if dot <= arr[middle]:
            end = middle - 1
        else:
            res = middle
            beg = middle + 1
    return res + 1


def main():
    section, dots = sys.stdin.readline().split()
    beg_list = []
    end_list = []
    for i in range(int(section)):
        beg, end = sys.stdin.readline().split()
        beg_list.append(int(beg))
        end_list.append(int(end))
    dot_list = list(map(int, sys.stdin.readline().split()))
    quicksort(beg_list, 0, len(beg_list) - 1)
    quicksort(end_list, 0, len(end_list) - 1)
    num_list = []
    for dot in dot_list:
        num = binary_search_beg(dot, beg_list) - binary_search_end(dot, end_list)
        num_list.append(str(num))
    print(" ".join(num_list))


if __name__ == '__main__':
    main()