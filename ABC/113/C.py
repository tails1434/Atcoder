def main():
    N, M = map(int, input().split())

    e = []
    for i in range(M):
        P, Y = map(int, input().split())
        e.append([i,P,Y])

    e.sort(key=lambda x : (x[1],x[2]))
    cnt = 1
    for i in range(M):
        if i == 0:
            e[i][1] = str(e[i][1]).zfill(6)
            e[i][2] = str(cnt).zfill(6)
            cnt += 1
        if int(e[i-1][1]) == e[i][1]:
            cnt += 1
            e[i][1] = str(e[i][1]).zfill(6)
            e[i][2] = str(cnt).zfill(6)
        else:
            cnt = 1
            e[i][1] = str(e[i][1]).zfill(6)
            e[i][2] = str(cnt).zfill(6)

    ans = sorted(e)
    for i,j,k in ans:
        print(j+k)

main()