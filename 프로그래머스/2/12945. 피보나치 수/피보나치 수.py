def solution(n):
    fb  = [0, 1]
    for i in range(2, n+1):
        fb.append(fb[i-1] + fb[i-2])
        
    answer = fb[-1]%1234567
    return answer