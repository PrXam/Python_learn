import time
import random


def best_decision(nums, available, probabilities):
    probability = 0
    index = None
    for i in range(nums - available+1):
        chance = sum(probabilities[i:i+available])
        if probability < chance:
            probability = chance
            index = i
    return index


def math_expect(nums, available, probabilities, index):
    probability = 0
    for i in range(index):
        probability += probabilities[i]
    for i in range(nums - index - available):
        probability += probabilities[index+available+i]
    print(probability)


with open('../input.txt', 'r') as file:
    nums = int(file.readline())
    available = int(file.readline())
    probabilities = file.readlines()
    probabilities = [random.random() for i in range(1000000)]
    timen = time.time()
    print(timen)
    probabilities = list(map(lambda x: float(x), probabilities))
    if available == 0:
        print(sum(probabilities))
    else:
        index = best_decision(nums, available, probabilities)
        if index is not None:
            math_expect(nums, available, probabilities, index)
        else:
            print(0)
print(time.time()-timen)
