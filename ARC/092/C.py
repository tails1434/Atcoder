def main():
    N = int(input())
    Red = []
    Blue = []
    for i in range(N):
        a, b = map(int, input().split())
        Red.append([b,a])
    for i in range(N):
        c, d = map(int, input().split())
        Blue.append([c,d])

    Red.sort(reverse=True)
    Blue.sort()
    ans = 0
    for x, y in Blue:
        for v, u in Red:
            if x > u and y > v:
                ans += 1
                Red.remove([v,u])
                break
    
    print(ans)

if __name__ == "__main__":
    main()