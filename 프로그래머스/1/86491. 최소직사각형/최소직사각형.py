def solution(sizes):
    width = []
    height = []
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            width.append(sizes[i][0])
            height.append(sizes[i][1])
        else:
            height.append(sizes[i][0])
            width.append(sizes[i][1])
        
    return max(width) * max(height)
