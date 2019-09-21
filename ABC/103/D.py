def main():
    N, M = map(int, input().split())
    query = []
    for _ in range(M):
        a, b = map(int, input().split())
        query.append([a,b])

    sort_query = sorted(query)

    cnt = 1
    left = 0
    right = float('inf')
    for i, j in sort_query:
        if max(left,i) >= min(right,j):
            cnt += 1
            left = i
            right = j
            continue
        left = max(left,i)
        right = min(right,j)

    print(cnt)
main()