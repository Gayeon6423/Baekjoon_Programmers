# 풀이1 : 시간 초과 발생
# A,B,V = map(int,input().split())
# day_cnt = 0
# distance = 0
# while True:
#     day_cnt += 1
#     if A * day_cnt - B * (day_cnt-1) >= V:
#         break
# print(day_cnt)

# 풀이2 : day_cnt 최소화
A,B,V = map(int,input().split())
day_cnt = (V-B)  / (A-B)
if day_cnt == int(day_cnt):
    print(int(day_cnt))
else:
    print(int(day_cnt)+1)