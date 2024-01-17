num_li = []
for _ in range(9):
    i = int(input())
    num_li.append(i)

print(max(num_li))
print(num_li.index(max(num_li))+1)