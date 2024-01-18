import sys
N,M = map(int, sys.stdin.readline().split())

num_li = []
for i in range(1,N+1):
    num_li.append(i)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    i_num = num_li[i-1]
    j_num = num_li[j-1]
    num_li[i-1] = j_num
    num_li[j-1] = i_num

for i in num_li:
    print(i,end = ' ')