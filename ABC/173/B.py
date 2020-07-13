from collections import defaultdict
def main():
    N = int(input())
    d = defaultdict(int)
    for _ in range(N):
        S = input()
        d[S] += 1

    for s in ['AC','WA','TLE','RE']:
        print(s + ' x ' + str(d[s]))
    



if __name__ == "__main__":
    main()