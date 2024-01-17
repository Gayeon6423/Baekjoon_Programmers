# 풀이1
import sys
N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

print(min(li), max(li))

# 풀이2
N = int(input())
li = list(map(int,input().split()))
max = li[0]
min = li[0]

for i in li[1:]:
    if i > max:
        max = i
    elif i < min:
        min = i
print(max, min)
