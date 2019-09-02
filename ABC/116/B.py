def main():
    s = int(input())
    num = [s]

    ans = 1

    for i in range(1000000):
        if num[i] % 2 == 0:
            num.append(num[i]//2)
            if len(set(num)) == ans:
                print(ans+1)
                exit()
            else:
                ans = len(set(num))
        else:
            num.append(num[i]*3+1)
            if len(set(num)) == ans:
                print(ans+1)
                exit()
            else:
                ans = len(set(num))



main()