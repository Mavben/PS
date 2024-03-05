def solution(name, yearning, photo):
    score_dict = dict(zip(name, yearning))
    
    result = [sum(score_dict.get(ch, 0) for ch in case) for case in photo]
    
    return result