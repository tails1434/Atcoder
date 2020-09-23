def primes(n):
    ass = []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    for i in range(len(is_prime)):
        if is_prime[i]:
            a = list(str(i))
            if a[-1] == '1':
                ass.append(i)
    return ass


def main():
    N = int(input())
    ass = primes(55555)
    ans = []
    for i in range(N):
        ans.append(ass[i])
    print(*ans)
    

if __name__ == "__main__":
    main()