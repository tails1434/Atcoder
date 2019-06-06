N = int(input())
A = [[int(i) for i in input().split()] for i in range(2)] 

tmp = 0

for i in range(N):
    list1 = A[0][:N-i]
    list2 = A[1][N-1-i:]
    if tmp < sum(list1) + sum(list2):
        tmp = sum(list1) + sum(list2)

print(tmp)