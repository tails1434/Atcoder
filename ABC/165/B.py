import sys
sys.setrecursionlimit(10000)

def main():
    X = int(input())
    A = 100
    cnt = 0
    while A < X:
        A *= 1.01
        A = int(A)
        cnt += 1

    print(cnt)



if __name__ == "__main__":
    main()