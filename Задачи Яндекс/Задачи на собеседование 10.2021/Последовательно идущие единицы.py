with open('input.txt', 'r') as f:
    num = f.readline()
    strin = 0
    len_str = 0
    for _ in range(int(num)):
        ch = f.readline().strip()
        if ch == '1':
            strin = strin + 1
            len_str = max(len_str, strin)
        else:
            strin = 0
    print(len_str)
