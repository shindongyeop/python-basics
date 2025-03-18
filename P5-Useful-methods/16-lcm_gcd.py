def gcd(n, m):
    gcd = []
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd.append(i)
    return max(gcd)

def lcm(n, m):
    return int((n * m) / gcd(n, m))

def solution(n, m):
    return [gcd(n, m), lcm(n, m)]

print(gcd(12, 18)) #6
print(lcm(12, 18)) #36
print(solution(3, 12)) #[3, 12]