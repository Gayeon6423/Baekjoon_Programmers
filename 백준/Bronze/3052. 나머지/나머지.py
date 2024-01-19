li = []
for _ in range(10):
    i = int(input())
    li.append(i % 42)
    
print(len(list(set(li))))