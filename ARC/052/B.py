from math import pi

def calc(r,h):
    return r ** 2 * pi * h / 3

def main():
    N, Q = map(int, input().split())
    V = [0] * (2 * 10 ** 4 + 5)
    for _ in range(N):
        X, R, H = map(int, input().split())
        for i in range(H):
            V[X + H - i] += calc(R * (i + 1) / H, i + 1) -calc(R * i / H, i)

    for i in range(len(V) - 1):
        V[i+1] += V[i]

    for _ in range(Q):
        A, B = map(int, input().split())
        print(V[B] - V[A])





if __name__ == "__main__":
    main()