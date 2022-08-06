def make_dict(s):
    a = dict()
    for i in s:
        count = s.count(i)
        a[i] = count
    return a


first_word = input()
second_word = input()

if make_dict(first_word) == make_dict(second_word):
    print(1)
else:
    print(0)