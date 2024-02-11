N = int(input())

x_li = []
y_li = []
for _ in range(N):
    x,y = map(int,input().split())
    x_li.append(x)
    y_li.append(y)

area = ((max(x_li)-min(x_li)) * (max(y_li)-min(y_li))) 
print(area)