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
            ass.append(i)
    return ass

def main():
    N = int(input())
    A = list(map(int, input().split()))
    max_A = max(A)
    ans = [0] * (max_A + 1)
    A.sort()
    for a in A:
        tmp = 1
        b = 0
        while b <= max_A:
            b = a * tmp
            if b > max_A:
                break
            ans[b] += 1
            tmp += 1
    cnt = 0
    for a in A:
        if ans[a] == 1:
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()