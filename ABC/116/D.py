import heapq

def main():
    N, K = map(int, input().split())
    sushi_list = []
    for _ in range(N):
        t, d = map(int, input().split())
        sushi_list.append((d,t))
    sushi_list = sorted(sushi_list, reverse=True)

    # 各種類(最大でK種類目まで)でおいしさが最大のものを保存
    keep = []
    # 取り替えるようのheapq
    exchange = []
    # keepに入っている種類
    types = set()
    for i in range(K):
        d, t = sushi_list[i]
        if t not in types:
            keep.append(d)
            types.add(t)
        else:
            heapq.heappush(exchange, d)

    base_point1 = sum(keep)
    base_point2 = sum(exchange)
    bonus_point = len(types)

    ans = base_point1 + base_point2 + bonus_point ** 2
    
    # K～N番目までをみて、選んでいない種類で最大のものを交換していく
    for i in range(K, N):
        if len(exchange) == 0:
            break

        d, t = sushi_list[i]
        # すでに選んだ種類のものはスキップする
        if t in types:
            continue 
        types.add(t)
        # 選んでいない種類で最大のものを追加する
        base_point1 += d
        # 選んだ種類で最小のものを削除する
        base_point2 -= heapq.heappop(exchange)
        bonus_point += 1
        ans = max(ans, base_point1 + base_point2 + bonus_point ** 2)

    print(ans)


    

main()