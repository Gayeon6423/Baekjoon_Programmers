def solution(array, commands):
    answer = []
    for command in commands:
        ans = sorted(array[command[0]-1:command[1]])[command[2]-1]
        answer.append(ans)
    return answer

