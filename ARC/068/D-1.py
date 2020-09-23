from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = set(A)
    if len(A) % 2 == 0:
        print(len(A) - 1)
    else:
        print(len(A))



if __name__ == "__main__":
    main()