s = input()
lst = '0123456789abcdefghijklmnopqrstuvwxyz'
ans = 0
for i in range(len(s)):
    ans += lst.index(s[i])*(35**i)
print(ans)
