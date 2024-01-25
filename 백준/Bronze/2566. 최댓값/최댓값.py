# 행렬 생성
matrix = []
for i in range(9):
    matrix.append(list(map(int, input().split())))
# 최대값 탐색
max_li = []
for i in range(9):
    max_li.append(max(matrix[i]))
max_value = max(max_li)
# 최대값 위치 탐색
for row, row_matrix in enumerate(matrix):
    if max_value in row_matrix:
        max_row = row
max_col = matrix[max_row].index(max_value)

print(max_value)
print(max_row + 1, max_col + 1)