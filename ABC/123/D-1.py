def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    AB = []
    for a in A:
        for b in B:
            AB.append(a + b)

    AB.sort(reverse=True)
    C.sort(reverse=True)
    ans = []
    for i in range(min(K,X*Y)):
        for j in range(min(K,Z)):
            ans.append(AB[i] + C[j])

    ans.sort(reverse=True)
    for k in range(K):
        print(ans[k])



if __name__ == "__main__":
    main()