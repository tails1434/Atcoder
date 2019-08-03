def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    N = int(input())
    T = [0] * N

    for i in range(N):
        T[i] = int(input())
    ans = T[0]
    for i in range(1, N):
        ans = ans * T[i] // gcd(ans, T[i])
    print(ans)


main()

