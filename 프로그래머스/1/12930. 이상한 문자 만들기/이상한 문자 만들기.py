def solution(s):
    answer = ''
    s_list = s.split(' ')
    
    for li in s_list:
        for i in range(len(li)):
            if not i % 2:
                answer += li[i].upper()
            else:
                answer += li[i].lower()
        answer += ' '
    
    return answer[:-1]
