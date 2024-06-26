def solution(s):
    answer = []
    
    # 이진 변환 횟수 변수
    cnt_binary = 0
    
    # 0의 개수
    cnt_zero = 0
    
    while 1:
        if s == "1":
            break
            
        cnt_binary += 1
        
        cnt_zero += s.count("0")
        
        s = s.replace("0", "")
        
        len_s = len(s)
        
        s = bin(len_s)[2:]
        
    answer.append(cnt_binary)
    answer.append(cnt_zero)
    
    return answer