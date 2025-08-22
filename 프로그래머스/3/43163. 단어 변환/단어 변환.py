# words에 있는 단어 사용해서 begin을 target으로 바꾸기
# 한번 변화할 때 한 단어만 변화 가능, 변환 횟수 출력
# 1. words에 target 없으면 바로 0 반환
# 2. 시작 단어부터 큐에 담기, 단계는 0으로 초기화
# 3. 해당 단어가 words의 단어들 중 1개의 알파벳값만 다르면 큐에 넣고 반복
# 4. target값을 찾으면 지금까지 세어준 단계 반환

from collections import deque
def bfs(begin, target, words):
    quque = deque()
    quque.append([begin,0]) # 시작 단어와 단계 0
    while quque:
        now_word, step = quque.popleft()
        if now_word == target:
            return step
        # 모든 단어 체크하면서, 해당 단어 변경될 수 있는지 확인
        for word in words:
            cnt = 0
            # 단어의 길이만큼 반복
            for i in range(len(word)):
                # 단어에 알파벳 한개씩 체크
                if now_word[i] != word[i]:
                    cnt += 1
            if cnt == 1:
                quque.append([word,step+1])
                



def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        return bfs(begin, target, words)