def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_a = max(a)
    ideal_comb = []
    if max_a % 2 == 0:
        ideal_comb.append(max_a // 2)
    else:
        ideal_comb.append(max_a // 2)
        ideal_comb.append(max_a // 2 + 1)

    diff = [0] * n

    for i in ideal_comb:
        for j in range(n):
            if a[j] == max_a:
                diff[j] += 10 ** 10
            else:
                diff[j] += abs(a[j] - i)

    tmp = diff.index(min(diff))

    print(max_a, a[tmp])

    


if __name__ == "__main__":
    main()