N = int(input())
# 2차원 배열 생성
ary = [[0 for _ in range(101)] for _ in range(101)]

# 배열에 해당하는 값 나오면 1로 값 변경
for _ in range(N):
    x,y = map(int, input().split())
    for row in range(x, x+10):
        for col in range(y,y+10):
            ary[row][col] = 1

# 검정색 영역 구하기 : 1의 개수 세기
area_sum = 0
for area in ary:
    area_sum += area.count(1)
print(area_sum)