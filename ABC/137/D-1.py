from heapq import heappush, heappop

def main():
    N, M = map(int, input().split())

    # 日数別に仕事を管理
    works = [[] for _ in range(M)]

    for i in range(N):
        A, B = map(int, input().split())
        
        if A > M:
            continue
        
        deadline = M - A
        # heapqは最小値を返す仕組みしかないので、最大値を返すため-する
        works[deadline].append(-B)
    
    ans = 0
    heapque = []

    # i日目に始めることができる仕事で報酬の高いものを選ぶ
    for i in range(M - 1, -1, -1):
        for work in works[i]:
            # heapqに候補を追加
            heappush(heapque, work)

        if heapque:
            ans += heappop(heapque)
    
    print(-ans)


main()