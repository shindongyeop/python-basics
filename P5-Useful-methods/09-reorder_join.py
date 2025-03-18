def solution(n):
    answer = 0
    array = str(n)
    new = "".join(sorted(array, reverse = True))
    answer = int(new)
    return answer

print(solution(118372))
      

def solution2(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))