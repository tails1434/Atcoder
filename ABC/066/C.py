from collections import deque
def main():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    b = deque(maxlen=n+1)
    for i in range(1,n+1):
        if (i % 2 == 0 and n % 2 == 0 ) or (i % 2 != 0 and n % 2 != 0 ):
            b.appendleft(a[i])
        else:
            b.append(a[i])

    print(*b)

main()