def merge(sub_arr1, sub_arr2, count):
    new_arr = []
    i, j = 0, 0
    while i < len(sub_arr1) and j < len(sub_arr2):
        if sub_arr1[i] <= sub_arr2[j]:
            new_arr.append(sub_arr1[i])
            i += 1
        else:
            new_arr.append(sub_arr2[j])
            j += 1
            count += (len(sub_arr1) - i)
    if i == len(sub_arr1):
        new_arr.extend(sub_arr2[j:])
    else:
        new_arr.extend(sub_arr1[i:])
    return new_arr, count


def main():
    n = input()
    queue = list(map(lambda x: [int(x)], input().split()))
    count = 0
    while len(queue) > 1:
        if len(queue[0]) < len(queue[1]):
            queue.append(queue.pop(0))
            continue
        else:
            elem1, elem2 = queue.pop(0), queue.pop(0)
        res, count = merge(elem1, elem2, count)
        queue.append(res)
    print(count)


if __name__ == "__main__":
    main()
