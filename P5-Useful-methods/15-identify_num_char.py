def solution(s):
    if len(s) not in (4,6):
        return False
    
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    
    return True

print(solution("1234")) # True
print(solution("1234a")) # False

def solution2(s):
    if not (len(s) == 4 or len(s) == 6):
        return False
    
    num_set = {'1', '2', '3', '4', '5',
               '6', '7', '8', '9', '0'}
    temp = set([i for i in s])
    print(temp)
    