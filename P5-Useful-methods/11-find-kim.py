def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return f"김서방은 {i}에 있다"

print(solution(["Jane", "Doe", "Kim"])) # "김서방은 1에 있다"