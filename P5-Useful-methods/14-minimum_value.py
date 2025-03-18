def solution(arr):
    # If the array has only on element, return [-1]
    answer = []
    if len(arr) == 1:
        return [-1]
    
    # Find the minimum value in the array
    min_value = min(arr)
    
    # Create a new list excluding the minimum value
    arr.remove(min_value)
   
    return arr

print(solution([4, 3, 2, 1])) # [4, 3, 2]
print(solution([10])) # [-1]