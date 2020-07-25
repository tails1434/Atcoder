def calc_triangle(A,B,C):
    S = abs((A[0] - C[0])*(B[1] - C[1]) - (B[0] - C[0])*(A[1]-C[1]))
    if S == 0:
        return False
    return S % 2 == 0

def main():
    N = int(input())
    points = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            for k in range(j+1,N):
                if calc_triangle(points[i],points[j],points[k]):
                    ans += 1

    print(ans)



if __name__ == "__main__":
    main()