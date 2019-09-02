def main():
    N = int(input())
    A = []
    for i in range(N):
        S, P = input().split()
        A.append((S,int(P),i+1))

    sort_A = sorted(A, key=lambda x:(x[0], -x[1])) 
    for i in range(N):
        print(sort_A[i][2])

main()