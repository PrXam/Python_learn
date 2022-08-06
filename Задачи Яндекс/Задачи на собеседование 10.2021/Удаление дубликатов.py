import sys
import bisect

a = []
prev_num = None
with open("input.txt", "r") as f:
    for _ in range(int(f.readline())):
        numi = int(f.readline())
        if numi != prev_num:
            prev_num = numi
            a.append(numi)

print(*(list(a)), sep="\n")
