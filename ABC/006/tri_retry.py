def tri(n):
    N = [] * n
    N[0] = 0
    N[1] = 0
    N[2] = 1
    for i in range(3, n):
        N[n] = (N[n-1] + N[n-2] + N[n-3]) % 10007 
    return N[n-1]

n = int(input())

print(tri(n))
