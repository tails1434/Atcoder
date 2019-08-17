def main():
    a, b = map(int, input().split())

    height = [0] * 1000

    for i in range(999):
        height[i+1] = height[i] + i + 1

    for i in range(1,999):
        diff_a = height[i] - a
        diff_b = height[i+1] - b
        if diff_a >= 0 and diff_b >= 0 and diff_a == diff_b:
            print(diff_a)
            exit()

main()