def solution(n):
    answer = []
    for i in reversed(str(n)):
        answer.append(int(i))
   
    return answer

print(solution(21345))