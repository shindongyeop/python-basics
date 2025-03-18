def solution(num):
    count = 0
    while num != 1:
        print(f'num is: {num}')
        if (num % 2 == 0):
            print(f'num before num / 2 operation is: {num}')
            num = num / 2
            print(f'num after num / 2 operation is: {num}')
            count += 1
            print(f'count is incremented to: {count}')
        else:
            print(f'num before num * 3 + 1 operation is: {num}')
            num = num * 3 + 1
            print(f'num after num * 3 + 1 operation is: {num}')
            count += 1
            print(f'count is incremented to: {count}')
            
        if count == 500:
            return -1
    return count

print(solution(6))



def solution2(num):
    count = 0
    for i in range (count):
        count += i
        if num % 2 == 0:
            num = num / 2
        elif num % 2 == 1:
            num = (num * 3) + 1
        elif num == 1: 
            break
        elif count == 500:
            return -1
    return count



def solution3(num):
    count = 0
    while count <= 500:
        if num % 2 == 0:
            num = num // 2
            count += 1
        else:
            num = (num * 3) + 1
            count += 1
        if num == 1:
            return count
    return -1
