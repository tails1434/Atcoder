from math import factorial

def combinations_count(n, r):
    ''' 組み合わせ '''
    return factorial(n) // (factorial(n - r) * factorial(r))

def max_ave():
    N, A, B = map(int, input().split())
    v = list(map(int, input().split()))
    sort_v = sorted(v, reverse=True)

    # 平均の最大値を求める
    sum_A = 0
    for i in range(A):
        sum_A += sort_v[i]
    max_ave_v = sum_A / A

    print(max_ave_v)

    # 選び方を求める
    V = sort_v[:A]
    num = v.count(min(V))
    a = V.count(min(V))
    cnt = 0
    if max(V) == min(V):
        for i in range(A,B+1):
            if num < i:
                continue
            cnt += combinations_count(num,i)
    else:
        cnt = combinations_count(num,a)
    
    print(cnt)

max_ave()