from heapq import heappop, heappush

def main():
    N, Q = map(int, input().split())
    # 幼稚園の数
    M = 2 * (10 ** 5)

    # 幼児iの所属先の幼稚園
    belong = [None] * N
    # 幼児iのレート
    rate = [None] * N

    # 幼稚園キュー (レート[降順], 幼児)
    Nur = [[] for _ in range(M)]

    for c in range(N):
        A, B = map(int, input().split())
        B -= 1
        belong[c] = B
        rate[c] = A
        heappush(Nur[B], (-A, c))

    # 最強園児の順序付きキュー
    q = []
    for i in range(M):
        if Nur[i]:
            A, c = Nur[i][0]
            heappush(q, (-A, c, i))
    
    for _ in range(Q):
        C, D = map(int, input().split())
        C -= 1
        D -= 1

        pre = belong[C]
        belong[C] = D

        # 移動元のキューを更新
        while Nur[pre]:
            A, c = Nur[pre][0]

            if belong[c] != pre:
                heappop(Nur[pre])
            else:
                heappush(q, (-A, c, pre))
                break

        heappush(Nur[D], (-rate[C], C))
        while Nur[D]:
            A, c = Nur[D][0]

            if belong[c] != D:
                heappop(Nur[D])
            else:
                heappush(q, (-A, c, D))
                break

        while q:
            A, c, d = q[0]
            if belong[c] != d or Nur[d][0][1] != c:
                heappop(q)
            else:
                print(A)
                break        





if __name__ == "__main__":
    main()