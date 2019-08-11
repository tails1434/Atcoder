from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))

    a = Counter(A)

    cnt = 0
    for i, num in a.items():
        if i < num:
            cnt += num - i
        elif i > num:
            cnt += num

    print(cnt)

main()