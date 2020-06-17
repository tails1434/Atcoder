def check(s1,s2,s3,s4,s5):
    if s1 == [1,2,3] and s2 == [1,3] and s3 == [1,3] and s4 == [1,3] and s5 == [1,2,3]:
        return '0'
    if s1 == [2] and s2 == [1,2] and s3 == [2] and s4 == [2] and s5 == [1,2,3]:
        return '1'
    if s1 == [1,2,3] and s2 == [3] and s3 == [1,2,3] and s4 == [1] and s5 == [1,2,3]:
        return '2'
    if s1 == [1,2,3] and s2 == [3] and s3 == [1,2,3] and s4 == [3] and s5 == [1,2,3]:
        return '3'
    if s1 == [1,3] and s2 == [1,3] and s3 == [1,2,3] and s4 == [3] and s5 == [3]:
        return '4'
    if s1 == [1,2,3] and s2 == [1] and s3 == [1,2,3] and s4 == [3] and s5 == [1,2,3]:
        return '5'
    if s1 == [1,2,3] and s2 == [1] and s3 == [1,2,3] and s4 == [1,3] and s5 == [1,2,3]:
        return '6'
    if s1 == [1,2,3] and s2 == [3] and s3 == [3] and s4 == [3] and s5 == [3]:
        return '7'
    if s1 == [1,2,3] and s2 == [1,3] and s3 == [1,2,3] and s4 == [1,3] and s5 == [1,2,3]:
        return '8'
    if s1 == [1,2,3] and s2 == [1,3] and s3 == [1,2,3] and s4 == [3] and s5 == [1,2,3]:
        return '9'

    

def main():
    N = int(input())
    s1 = input()
    s2 = input()
    s3 = input()
    s4 = input()
    s5 = input()
    ans = ''
    left = 0
    right = 5
    cnt = 0
    while cnt < N:
        s1_cnt = []
        s2_cnt = []
        s3_cnt = []
        s4_cnt = []
        s5_cnt = []
        for i in range(left, right):
            if s1[i] == '#':
                s1_cnt.append(i%4)
            if s2[i] == '#':
                s2_cnt.append(i%4)
            if s3[i] == '#':
                s3_cnt.append(i%4)
            if s4[i] == '#':
                s4_cnt.append(i%4)
            if s5[i] == '#':
                s5_cnt.append(i%4)

        ans += check(s1_cnt, s2_cnt, s3_cnt, s4_cnt, s5_cnt)
        cnt += 1
        left += 4
        right += 4

    print(ans)

    

if __name__ == "__main__":
    main()