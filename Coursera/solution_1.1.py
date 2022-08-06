import sys

digit_string = sys.argv[1]

summ = 0
for num in digit_string:
    summ += int(num)
print(summ)    