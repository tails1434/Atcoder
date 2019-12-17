from itertools import accumulate

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def main():
    N = [0] * (10 ** 5 + 1)
    for i in range(3, 10 ** 5 + 1, 2):
        if is_prime(i) and is_prime((i + 1) // 2):
            N[i] += 1

    A = list(accumulate(N))
    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        l -= 1
        print(A[r] - A[l])




if __name__ == "__main__":
    main()