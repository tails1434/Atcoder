N = input()
reverse_N = ''.join(list(reversed(N)))

if N == reverse_N:
    print('Yes')
else:
    print('No')