import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
k=0
for i in b:
    if i in a:
        k+=1
print(k)