from collections import Counter
x_li = []
y_li = []
for _ in range(3):
    x,y = map(int, input().split())
    x_li.append(x)
    y_li.append(y)

# 개수가 1개인 좌표값을 x좌표로 지정
x_dict = dict(Counter(x_li))
for key,value in x_dict.items():
    if value == 1:
        x_loc = key
# 개수가 1개인 좌표값을 y좌표로 지정
y_dict = dict(Counter(y_li))
for key, value in y_dict.items():
    if value == 1:
        y_loc = key

print(x_loc, y_loc)