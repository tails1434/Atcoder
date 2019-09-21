def main():
    N, H = map(int, input().split())

    A = [0] * N
    B = [0] * N

    num_list = []
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b

    sort_B = sorted(B, reverse=True)
    max_A = max(A)
    ans = 0
    for b in sort_B:
        if b > max_A:
            ans += 1
            H -= b
        else:
            break
        
        if H <= 0:
            break
    
    if H > 0:
        ans += -(-H // max_A)

    print(ans)

main()