def main():
    X, Y = map(int, input().split())
    if X % Y == 0:
        print(-1)
    else:
        print(X)



if __name__ == "__main__":
    main()