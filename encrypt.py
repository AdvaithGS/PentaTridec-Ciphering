s = input('Enter normal text: ')
lst = '0123456789abcdefghijklmnopqrstuvwxyz '
ans = 0
for i in range(len(s)):
    ans += lst.index(s[i])*(37**i)
print(ans)
