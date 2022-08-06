from collections import Counter


def calc():
    code = input()
    count = Counter(code)
    encode = {}
    if len(count) == 1:
        encode[count.popitem()[0]] = '0'
    for i in range(len(count) - 1):
        first = count.most_common()[-1]
        count.pop(first[0])
        for let in first[0]:
            if encode.get(let):
                encode[let] = '0' + encode[let]
            else:
                encode[let] = '0'
        second = count.most_common()[-1]
        count.pop(second[0])
        for let in second[0]:
            if encode.get(let):
                encode[let] = '1' + encode[let]
            else:
                encode[let] = '1'
        count[first[0] + second[0]] = first[1] + second[1]
    for key, value in encode.items():
        code = code.replace(key, value)
    print(len(encode), len(code))
    for key, value in encode.items():
        print(key, ': ', value, sep='')
    print(code)


if __name__ == '__main__':
    calc()