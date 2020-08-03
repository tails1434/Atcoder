def main():
    N = int(input())
    s = list(input())
    for t0,t1 in [('S','S'),('S','W'),('W','S'),('W','W')]:
        T = ['S'] * (N + 1)

        T[0] = t0
        T[1] = t1

        for i in range(1,N):
            if s[i] == 'o':
                if T[i] == 'S':
                    T[i+1] = T[i-1]
                else:
                    if T[i-1] == 'W':
                        T[i+1] = 'S'
                    else:
                        T[i+1] = 'W'
            else:
                if T[i] == 'W':
                    T[i+1] = T[i-1]
                else:
                    if T[i-1] == 'W':
                        T[i+1] = 'S'
                    else:
                        T[i+1] = 'W'

        if T[-1] == T[0]:
            if T[0] == 'S':
                if s[0] == 'o' and T[-2] == T[1]:
                    T.pop(-1)
                    print(''.join(T))
                    exit()
                elif s[0] == 'x' and T[-2] != T[1]:
                    T.pop(-1)
                    print(''.join(T))
                    exit()
            else:
                if s[0] == 'x' and T[-2] == T[1]:
                    T.pop(-1)
                    print(''.join(T))
                    exit()
                elif s[0] == 'o' and T[-2] != T[1]:
                    T.pop(-1)
                    print(''.join(T))
                    exit()


    print(-1)



if __name__ == "__main__":
    main()