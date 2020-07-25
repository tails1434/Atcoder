from collections import Counter

def main():
    S1 = input()
    S2 = input()
    S3 = input()

    C1 = Counter(S1)
    C2 = Counter(S2)
    C3 = Counter(S3)
    L = 0
    R = 0
    for i in range(26):
        x = chr(ord('A') + i)
        L += max(0, C3[x] - C2[x])
        R += min(C1[x], C3[x])

    if L <= len(S3) // 2 <= R:
        print('YES')
    else:
        print('NO')

if __name__ == "__main__":
    main()