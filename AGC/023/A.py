from itertools import accumulate
from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] + list(accumulate(A))
    C = Counter(B)
    ans = 0
    for i in C.values():
        ans += i * (i - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()