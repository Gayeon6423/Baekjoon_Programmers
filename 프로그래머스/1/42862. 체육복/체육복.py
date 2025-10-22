# def solution(n,lost,reserve):
#     clo = [1 for i in range(n)]
#     for i in lost:
#         clo[i-1] = clo[i-1] - 1
#     for i in reserve:
#         clo[i-1] = clo[i-1] + 1
#     for i in range(n):
#         if clo[i] == 0:
#             if i > 0 and clo[i-1] == 2:
#                 clo[i] = 1
#                 clo[i-1] = 1
#             elif i < n-1 and clo[i+1] == 2:
#                 clo[i] = 1
#                 clo[i+1] = 1
#     clo = [1 if c >= 2 else c for c in clo]
#     ans = sum(clo)
#     return ans


# def solution(n,lost,reverse):
#     clo_sum = 0
#     clo = [1 for i in range(n)]
#     for l in lost:
#         clo[l-1] = 0
#     for r in reverse:
#         clo[r-1] = 2
        
#     for idx, c in enumerate(clo):
#         if idx == 0:
#             if c == 0 and clo[idx+1] == 2:
#                 clo[idx] = 1
#                 clo[idx+1] = 1
#         elif idx >= 1 and idx <= n-2:
#             if clo[idx-1] == 2:
#                 clo[idx] = 1
#                 clo[idx-1] = 1
#             elif clo[idx+1] == 2:
#                 clo[idx] = 1
#                 clo[idx+1] = 1
#         elif idx == n-1:
#             if clo[idx-1] == 2:
#                 clo[idx] = 1
#                 clo[idx-1] = 1
#     clo = [1 if c == 2 else c for c in clo]
#     clo_sum = sum(clo)
#     print(clo)
#     return clo_sum    

# def solution(n,lost,reserve):
#     clo = [1 for c in range(0,n)]
#     for l in lost:
#         clo[l-1] -= 1
#     for r in reserve:
#         clo[r-1] += 1
#     for i, c in enumerate(clo): 
#         if (clo[i] == 0) and (clo[i-1] == 2):
#             clo[i] = 1
#             clo[i-1] = 1
#         elif (clo[i] == 0) and (clo[i+1] == 2):
#             clo[i] = 1
#             clo[i+1] = 1
#     for c in clo:
#         if c > 1:
#             clo[clo.index(c)] = 1
#     clo_sum = sum(clo)
#     return clo_sum
    
def solution(n,lost,reserve):
    clo = [1 for i in range(n)]
    for l in lost:
        clo[l-1] -= 1
    for r in reserve:
        clo[r-1] += 1
    for i,c in enumerate(clo):
        if clo[i] == 0:
            if i==0 and clo[i+1] == 2:
                clo[i] += 1
                clo[i+1] -= 1 
            elif i > 0 and i < n-1:
                if clo[i-1] == 2:
                    clo[i] += 1
                    clo[i-1] -= 1
                elif clo[i+1] == 2:
                    clo[i] += 1
                    clo[i+1] -= 1
            elif i==n-1 and clo[i-1] == 2:
                clo[i] +=  1
                clo[i-1] -= 1
                
    clo = [1 if c == 2 else c for c in clo]
    ans = sum(clo)

    return ans