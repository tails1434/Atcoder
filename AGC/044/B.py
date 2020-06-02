def func(x):
    return x - 1

def main():
    N = int(input())
    P = list(map(func, map(int, input().split())))
    seki = [[0] * N for _ in range(N)]

    for p in P:
        div = p // N
        mod = p % N
        seki[div][mod] = p
    
    ans = 0
    
        



if __name__ == "__main__":
    main()