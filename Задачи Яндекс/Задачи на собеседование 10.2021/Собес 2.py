def prog(lst):
    lst.sort()
    start = 0
    s = str(lst[0])
    for i in range(len(lst)-1):
        if lst[i+1] != lst[i] + 1 and i - start>0:
            s+= '-' + str(lst[i]) + ',' + str(lst[i+1])
            start = i+1
        elif lst[i+1] != lst[i] + 1 and i - start==0:
            s+= ',' + str(lst[i+1])
            start = i+1
        elif lst[i+1] == lst[i] + 1 and lst[i+1] == lst[-1]:
            s+= '-' + str(lst[i+1])
        else:
            continue
    print(s)

prog([1,2,3,4, 6])