def solution(s):
    # 문자열 s를 정렬시키기 위해 int형 리스트로 변환
    # answer [0]과 answer[-1]을 이용해 최솟값고 최댓값 가져옴
    answer = list(map(int, s.split(' ')))
    answer.sort()
    return str(answer[0]) + ' ' + str(answer[-1])
