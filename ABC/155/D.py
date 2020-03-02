from bisect import bisect

def countPairs(a, n, mid):
    res = 0
    for i in range(n):
        res += bisect(a, mid // a[i])

    return res

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    high = 10 ** 20 
    if A[0] < 0:
        low = A[0] * A[-1]
    else:
        low = A[0] * A[1]
    
    while low < high:
        mid = (low + high) // 2
        count = 0
        left = 0
        for right in range(N):
            print(right, left)
            while A[right] * A[left] > mid:
                left += 1
            count += right - left
        
        if count >= K:
            high = mid
        else:
            low = mid + 1

    print(low)



if __name__ == "__main__":
    main()