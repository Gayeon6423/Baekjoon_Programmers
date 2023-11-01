## Hash 이용
# HashDict : Key-Value 의 Pair를 관리하는 딕셔너리
# Key : hash 함수 결과, Value : 각 선수 이름
def solution(participant, completion):
    HashDict = {}
    SumHash = 0

    for part in participant:
        # 1. HashMap : Participant의 Key-Value dict 구현
        HashDict[hash(part)] = part
        # 2. SumHash : Participant의 sum(hash) 계산
        SumHash += hash(part)

    # 3. Completion의 sum(hash)를 빼기
    for comp in completion:
        SumHash -= hash(comp)

    # 4. HashDict에 남아 있는 값이 완주하지 못한 선수의 hash값
    return HashDict[SumHash]