def solution(n):
    if (n**0.5) == int(n**0.5):
        return int((n**0.5+1)**2)
    else:
        return -1
    
print(solution(121))


def solution2(n):
    x = int(n ** 0.5)
    if n ** 0.5 == x:
        return (x + 1) ** 2
    else:
        return -1