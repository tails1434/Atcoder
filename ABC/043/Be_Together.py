N = int(input())
a = input().split(" ")

sum_a = []
for j in range(-100, 101):
    result = 0
    for i in a:
        result += (int(i) - j) ** 2
    sum_a.append(result)

print(min(sum_a))
