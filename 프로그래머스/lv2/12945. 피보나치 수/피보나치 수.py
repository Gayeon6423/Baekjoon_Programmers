def solution(n):
    fibo = [0,1] # f(0) = 0, f(1) = 1
   
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2]) # f(n) = f(n-1) + f(n-2)
    
    answer = fibo[-1] % 1234567 # 나머지 return
    return answer
        
solution(55)