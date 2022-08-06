import sys


def siftdown(list_prior):
    n = len(list_prior)
    iteration = 0
    while n > 1:
        n //= 2
        iteration += 1
    max_num = 0
    now = 0
    n = len(list_prior) - 1
    for k in range(iteration):
        exist1 = 2 * (max_num + 1) - 1
        exist2 = 2 * (max_num + 1)
        if exist1 > n:
            break
        elif exist2 > n:
            exist2 = exist1
        if list_prior[now] < list_prior[exist1]:
            max_num = exist1
        if list_prior[now] < list_prior[exist2] and list_prior[max_num] < list_prior[exist2]:
            max_num = exist2
        if list_prior[now] != list_prior[max_num]:
            list_prior[now], list_prior[max_num] = list_prior[max_num], list_prior[now]
            now = max_num
        else:
            break


def insert(list_prior, num):
    list_prior.append(num)
    index = len(list_prior)
    while index > 1:
        if list_prior[index - 1] > list_prior[index // 2 - 1]:
            list_prior[index - 1], list_prior[index // 2 - 1] = list_prior[index // 2 - 1], list_prior[index - 1]
            index = index // 2
        else:
            break
    return 0


def extract_max(list_prior):
    list_prior[0], list_prior[-1] = list_prior[-1], list_prior[0]
    elem = str(list_prior.pop())
    siftdown(list_prior)
    return elem


def main():
    number = int(sys.stdin.readline())
    list_prior = []
    for i in range(number):
        operation = sys.stdin.readline()
        if 'Insert' in operation:
            insert(list_prior, int(operation.split()[1]))
        if 'Extract' in operation:
            sys.stdout.write(extract_max(list_prior) + '\n')


if __name__ == '__main__':
    main()