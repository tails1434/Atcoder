def isOK(a,index,key):
    if a[index] >= key:
        return True
    else:
        return False

def binary_search(a,key):
    ng = -1
    ok = len(a)

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2

        if isOK(a,mid,key):
            ok = mid
        else:
            ng = mid

        return ok

def main():
    N = int(input())
    L = list(map(int, input().split()))
    sort_L = sorted(L)
    cnt = 0
    for i in range(N-2):
        for j in range(i+1,N-1):
            tmp = sort_L[i] + sort_L[j]
            print(i,j)
            a = binary_search(sort_L,tmp)
            print(a)



if __name__ == "__main__":
    main()