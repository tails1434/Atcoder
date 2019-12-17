from collections import defaultdict, deque

def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                a = 0
                password = str(i) + str(j) + str(k)
                for s in S:
                    if s == password[a]:
                        a += 1
                    if a == 3:
                        ans += 1
                        break

    print(ans)


if __name__ == "__main__":
    main()