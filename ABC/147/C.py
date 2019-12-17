import sys
input = sys.stdin.readline

def main():
    N = int(input())
    A = [0] * N
    X = [[]  for _ in range(N)]
    for i in range(N):
        A[i] = int(input())
        for _ in range(A[i]):
            x, y = map(int, input().split())
            x -= 1
            X[i].append((x,y))

    ans = 0
    for i in range(1<<N):
        T = []
        F = []
        for j in range(N):
            if (i>>j) & 1:
                T.append(j)
            else:
                F.append(j)
        flag = False
        for t in T:
            for x, y in X[t]:
                if y == 1:
                    if x in F:
                        flag = True
                        break
                else:
                    if x in T:
                        flag = True
                        break
            if flag:
                break
        if not flag:
            ans = max(ans, len(T))

    print(ans)





if __name__ == "__main__":
    main()