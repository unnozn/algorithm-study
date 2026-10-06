def solution(strArr):
    count = {}
    
    for s in strArr:
        length = len(s)
        
        if length not in count:
            count[length] = 0
            
        count[length] += 1
        
    return max(count.values())