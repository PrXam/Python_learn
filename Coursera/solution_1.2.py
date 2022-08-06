import sys

num = int(sys.argv[1])
k = num
while k > 0:
    k -= 1
    print(" "*k+"#"*(num-k))

