def main():
    N = int(input())
    a = list(map(int, input().split()))

    cnt = [0] * 100002

    for i in a:
        cnt[i-1] += 1
        cnt[i] += 1
        cnt[i+1] += 1
    
    print(max(cnt))

main()