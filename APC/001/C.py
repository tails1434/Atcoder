def main():
    N = int(input())
    print(0, flush=True)
    s = input()
    if s == 'Vacant':
        exit()
    ans = [''] * N
    ans[0] = s
    pre = 0
    left = 0
    right = N
    while True:
        mid = (right + left) // 2
        print(mid, flush=True)
        s = input()
        ans[mid] = s
        if s == 'Vacant':
            exit()
        cnt = abs(mid - pre)
        if cnt % 2 == 0:
            if ans[pre] == ans[mid]:
                #間には存在しない
                if pre > mid:
                    right = mid
                else:
                    left = mid
            else:
                #間には存在する
                if pre > mid:
                    left = mid
                else:
                    right = mid
        else:
            if ans[pre] == ans[mid]:
                #間には存在する
                if pre > mid:
                    left = mid
                else:
                    right = mid
            else:
                #間には存在しない
                if pre > mid:
                    right = mid
                else:
                    left = mid
        pre = mid

        


if __name__ == "__main__":
    main()