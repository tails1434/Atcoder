def main():
    A, B, K = map(int, input().split())
    C = max(A - K , 0)
    K = max(K - A , 0)
    D = max(B - K , 0)
    print(C, D)



if __name__ == "__main__":
    main()