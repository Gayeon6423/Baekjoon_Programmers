def solution(n,lost,reverse):
    anwer = 0
    clothes = [1 for i in range(n)] # 모든 학생으느 체육복 하나 가지고 있는 상태

    # 도난당한 학생의 체육복 상태 업데이트
    for i in lost:
        clothes[i-1] = clothes[i-1] - 1

    # 여벌의 체육복 가져온 학생의 체육복 상태 업데이트    
    for i in reverse:
        clothes[i-1] = clothes[i-1] + 1

    # 체육복 빌려주기
    for i in range(n):
        if clothes[i] == 0:
            if i > 0 and clothes[i-1] == 2: # 앞번호 학생이 여벌의 체육복 가지고 있으면
                clothes[i] = 1
                clothes[i-1] = 1
            
            elif i < n-1 and clothes[i+1] == 2: # 뒷번호 학생이 여벌의 체육복 가지고 있으면
                clothes[i] = 1
                clothes[i+1] = 1
            
    # 체육수업 들을 수 있는 학생 수
    answer  = sum(1 for c in clothes if c>=1) # 여벌 체육복도 1로 고려
    return answer