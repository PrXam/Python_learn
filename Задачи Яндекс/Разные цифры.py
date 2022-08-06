def search_num(amount, nums):
    list_num = nums.split()
    for i in range(amount):
        for j in range(amount):
            for k in range(amount):
                if i != j and i != k and j != k:
                    set_num = set(list_num[i] + list_num[j] + list_num[k])
                    if len(set_num) == 10:
                        print(int(list_num[i]), int(list_num[j]),int(list_num[k]))
                        return 0


with open('../input.txt', 'r') as file:
    iter_num = file.readline()
    for i in range(int(iter_num)):
        amount = int(file.readline())
        nums = file.readline()
        list_num =(search_num(amount, nums))