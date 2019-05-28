N = int(input())
N %= 30

print(N)
list1 = [1, 2, 3, 4, 5, 6]


for i in range(N):
    a = int(i % 5)
    list1[a], list1[a+1] = list1[a+1], list1[a]

for s in list1:
  print(s, end ="")