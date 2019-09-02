import fractions


def main():
    N = int(input())
    A = list(map(int, input().split()))

    gcd_ans = []
 
    l = [0] * N
    r =[0] * N
    for i in range(N-1):
        l[i+1] = fractions.gcd(l[i],A[i])
        r[i+1] = fractions.gcd(r[i],A[N-1-i])
    r.reverse()
 
    for i in range(N):
        gcd_ans.append(fractions.gcd(l[i],r[i]))
 
    print(max(gcd_ans))


main()