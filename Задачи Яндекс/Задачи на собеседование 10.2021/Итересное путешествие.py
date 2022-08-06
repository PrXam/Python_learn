import sys


num = int(sys.stdin.readline().strip())
towns = []
for _ in range(num):
    towns.append(sys.stdin.readline().strip().split())
limit = int(sys.stdin.readline().strip())
index = sys.stdin.readline().strip().split()
start = towns[int(index[0])-1]
end = towns[int(index[1])-1]
towns = sorted(towns, key=lambda x: abs(int(x[0])) + abs(int(x[1])))
start_index = towns.index(start)
end_index = towns.index(end)
if start_index > end_index:
    start_index, end_index = end_index, start_index
iterate = 0
middle_index = end_index
print(towns)
while start_index != end_index:

    distance = abs(int(towns[middle_index][0]) - int(towns[start_index][0])) + \
               abs(int(towns[middle_index][1]) - int(towns[start_index][1]))
    if distance <= limit:
        iterate += 1
        start_index = middle_index
        middle_index = end_index
    elif middle_index != start_index+1:
         middle_index -= 1
    else:
        iterate = -1
        break
print(iterate)
