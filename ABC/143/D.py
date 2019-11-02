import bisect

def main():
    N = int(input())
    L = list(map(int, input().split()))
    sort_L = sorted(L)
    cnt = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            tmp = bisect.bisect_left(sort_L,sort_L[i] + sort_L[j])
            if tmp - 1 > j:
                cnt += tmp - j - 1
    print(cnt)

    

if __name__ == "__main__":
    main()