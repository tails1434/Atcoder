from math import gcd

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    S = list(map(int, input().split()))
    a = A[0]
    B = [0]
    for i in range(1,N):
        tmp = gcd(a,A[i])
        if a != tmp:
            B.append(i)
        a = tmp

    
    for s in S:
        X = gcd(s,a)
        if X == 1:
            X = s

        
            for i in B:
                X = gcd(X, A[i])
                if X == 1:
                    print(i + 1)
                    break
        else:
            print(X)


if __name__ == "__main__":
    main()