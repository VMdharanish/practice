def sieve(n):
    prime = [True] * (n + 1)
    p = 2

    while p * p <= n:
        if prime[p]:
            
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1

    arr = []
    for i in range(2, n + 1):
        if prime[i]:
            arr.append(p)
    
    return arr
