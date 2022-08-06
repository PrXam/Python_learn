def main():
    num = int(input())
    step_list = list(map(int, input().split()))
    if num > 1:
        sum_list = [step_list[0], max(step_list[1], step_list[0] + step_list[1])]
        for step in range(2, num):
            sum_list.append(max(step_list[step] + sum_list[step - 1], step_list[step] + sum_list[step - 2]))
        print(sum_list[-1])
    else:
        print(step_list[0])


if __name__ == '__main__':
    main()