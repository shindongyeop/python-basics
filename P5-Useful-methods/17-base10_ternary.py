def solution(n):
    # Convert n to base 3 (ternary) as a string
    answer = 0
    ternary = ""
    while n > 0:
        ternary = str(n % 3) + ternary
        print(f"n: {n}, after ternary = {n} % 3 + ternary, ternary = {ternary}")
        n = n // 3 
        print(f"n: {n}, after n = {n} // 3, n: {n}")
    
    # Reverse the ternary representation    
    reversed_ternary = ternary[:: -1] 
    
    # Convert back to decimal (base 10)
    decimal_result = int(reversed_ternary, 3)  
            
    return decimal_result

print(solution(45))