# 삼각형 꼭대기부터 아래로 내려가며 숫자 선택
# 내려갈 때 바로 아래 or 오른쪽 아래 칸만 선택
# 맨 아래 도착했을 때, 선택된 숫자 합이 최대가 되도록 경로 고름
# 위에서 내려올 수 있는 경로 중 최댓값만 더해가면서 마지막 줄까지 갱신하고, 그 최댓값을 결과로 반환
# 아래로 내려가며 최대 누적합 갱신하기
# 상향식 방식(Bottom-Up)


def solution(triangle):
    dp = triangle # 삼각형을 dp 테이블로 사용
    depth = len(dp)
    for i in range(1,depth): # 두 번째 줄(인덱스1)부터 시작
        # print('i:',i)
        for j in range(i+1): # 해당 줄의 모든 원소 탐색
            # print('j:',j)
            if j == 0: # 맨 왼쪽 끝
                dp[i][j] += dp[i-1][j] # 위에서만 내려올 수 있음
            elif j == i: # 맨 오른쪽 끝
                dp[i][j] += dp[i-1][j-1] # 왼쪽에서만 내려올 수 있음
            else: # 중간 위치
                dp[i][j] += max(dp[i-1][j],dp[i-1][j-1]) # 위의 값 or 왼쪽 위의 값
    max_sum = max(dp[depth-1])
    return max_sum