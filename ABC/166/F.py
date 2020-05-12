def main():
    N, A, B, C = map(int, input().split())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)

    D = [0] * 3
    ans = [''] * N
    for i in range(N):
        if S[i] == 'AB':
            if A >= B:
                if A <= 0:
                    A += 2
                    if D[0] >= 1 and D[1] >= 1:
                        if B >= C:
                            if B > 1:
                                B -= 2
                            else:
                                print('No')
                                exit()
                        else:
                            if C > 1:
                                C -= 2
                            else:
                                print('No')
                                exit()
                    elif D[0] >= 1:
                        if B > 1:
                            B -= 2
                        else:
                            print('No')
                            exit()
                    elif D[1] >= 1:
                        if C > 2:
                            C -= 2
                        else:
                            print('No')
                            exit()
                    else:
                        print('No')
                        exit()
                A -= 1
                B += 1
                ans[i] = 'B'
                D[0] += 1
            else:
                if B <= 0:
                    B += 2
                    if D[0] >= 1 and D[2] >= 1:
                        if A >= C:
                            if A > 1:
                                A -= 2
                            else:
                                print('No')
                                exit()
                        else:
                            if C > 1:
                                C -= 2
                            else:
                                print('No')
                                exit()
                    elif D[0] >= 1:
                        if A > 1:
                            A -= 2
                        else:
                            print('No')
                            exit()
                    elif D[2] >= 1:
                        if C > 1:
                            C -= 2
                        else:
                            print('No')
                            exit()
                    else:
                        print('No')
                        exit()
                A += 1
                B -= 1
                ans[i] = 'A'
                D[0] += 1
        if S[i] == 'AC':
            if A >= C:
                if A <= 0:
                    A += 2
                    if D[0] >= 1 and D[1] >= 1:
                        if B >= C:
                            if B > 1:
                                B -= 2
                            else:
                                print('No')
                                exit()
                        else:
                            if C > 1:
                                C -= 2
                            else:
                                print('No')
                                exit()
                    elif D[0] >= 1:
                        if B > 1:
                            B -= 2
                        else:
                            print('No')
                            exit()
                    elif D[1] >= 1:
                        if C > 2:
                            C -= 2
                        else:
                            print('No')
                            exit()
                    else:
                        print('No')
                        exit()
                A -= 1
                C += 1
                ans[i] = 'C'
                D[1] += 1
            else:
                if C <= 0:
                    C += 2
                    if D[1] >= 1 and D[2] >= 1:
                        if A >= B:
                            if A > 1:
                                A -= 2
                            else:
                                print('No')
                                exit()
                        else:
                            if B > 1:
                                B -= 2
                            else:
                                print('No')
                                exit()
                    elif D[1] >= 1:
                        if A > 1:
                            A -= 2
                        else:
                            print('No')
                            exit()
                    elif D[2] >= 1:
                        if B > 1:
                            B -= 2
                        else:
                            print('No')
                            exit()
                    else:
                        print('No')
                        exit()
                A += 1
                C -= 1
                ans[i] = 'A'
                D[1] += 1
        if S[i] == 'BC':
            if B >= C:
                if B <= 0:
                    B += 2
                    if D[0] >= 1 and D[2] >= 1:
                        if A >= C:
                            if A > 1:
                                A -= 2
                            else:
                                print('No')
                                exit()
                        else:
                            if C > 1:
                                C -= 2
                            else:
                                print('No')
                                exit()
                    elif D[0] >= 1:
                        if A > 1:
                            A -= 2
                        else:
                            print('No')
                            exit()
                    elif D[2] >= 1:
                        if C > 2:
                            C -= 2
                        else:
                            print('No')
                            exit()
                    else:
                        print('No')
                        exit()
                B -= 1
                C += 1
                ans[i] = 'C'
                D[2] += 1
            else:
                if C <= 0:
                    C += 2
                    if D[1] >= 1 and D[2] >= 1:
                        if A >= B:
                            if A > 1:
                                A -= 2
                            else:
                                print('No')
                                exit()
                        else:
                            if B > 1:
                                B -= 2
                            else:
                                print('No')
                                exit()
                    elif D[1] >= 1:
                        if A > 1:
                            A -= 2
                        else:
                            print('No')
                            exit()
                    elif D[2] >= 1:
                        if B > 1:
                            B -= 2
                        else:
                            print('No')
                            exit()
                    else:
                        print('No')
                        exit()
                B += 1
                C -= 1
                ans[i] = 'B'
                D[1] += 1

if __name__ == "__main__":
    main()