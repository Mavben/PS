def solution(keymap, targets):
    answer = []

    keymap_dic = {}
    for key in keymap:
        for idx,k in enumerate(key):
            if (k not in keymap_dic.keys()) or (k in keymap_dic.keys() and keymap_dic[k] > idx):  
                keymap_dic[k] = idx+1
    
    for target in targets:
        temp = 0
        for k in target:
            if k not in keymap_dic.keys():
                temp = -1
                break
            temp += keymap_dic[k]
        answer.append(temp)
    return answer