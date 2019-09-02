import fractions
import functools

def main():
    N, X = map(int, input().split())
    x = [X] + list(map(int, input().split()))
 
    sort_x = sorted(x)
    diff = [0] * N
    for i in range(N):
        diff[i] = sort_x[i + 1] - sort_x[i]

    ans = functools.reduce(fractions.gcd, diff)

    print(ans)

    


main()