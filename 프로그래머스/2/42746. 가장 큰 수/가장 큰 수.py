def solution(numbers):
    ans = ''
    numbers = list(map(str,numbers)) # string으로 바꾸어 비
    numbers.sort(key=lambda x:x*3, reverse=True) # 3번씩 반복한값 비
    ans = ''.join(numbers)
    return str(int(ans))

numbers = [6,10,2]
solution(numbers)
