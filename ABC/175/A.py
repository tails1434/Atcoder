def main():
    S = input()
    if S.count('R') == 0:
        print(0)
        exit()
    cnt = 1
    for i in range(2):
        if S[i] == 'R' and S[i+1] == 'R':
            cnt += 1 

    print(cnt)

if __name__ == "__main__":
    main()