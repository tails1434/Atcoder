def main():
    N = int(input())
    A = list(map(int, input().split()))
    money = 1000
    kab = 0
    cand = [A[0]]
    pre = A[0]
    for i in range(1,N):
        if A[i] < pre:
            cand.append(A[i-1])
            cand.append(A[i])
        pre = A[i]
    if pre <= A[-1]:
        cand.append(A[-1])
    if len(cand) % 2 == 1:
        cand.pop(-1)
    for i in range(len(cand)):
        if i % 2 == 0:
            cnt = money // cand[i]
            kab += cnt
            money -= cand[i] * cnt 
        else:
            money += cand[i] * kab
            kab = 0
    
    print(money)

if __name__ == "__main__":
    main()