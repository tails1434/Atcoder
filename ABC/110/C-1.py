from collections import Counter

def main():
    S = input()
    T = input()
    cnt_S = []
    cnt_T = []
    for i, j in Counter(S).items():
        cnt_S.append(j)
    for i, j in Counter(T).items():
        cnt_T.append(j)

    cnt_S.sort()
    cnt_T.sort()
    if cnt_T == cnt_S:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()