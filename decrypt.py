s = int(input('Enter encrypted text: '))
i = 0
while 37**i < s:
    i += 1
i -= 1
def convert(n):
    lst = '0123456789abcdefghijklmnopqrstuvwxyz '
    return lst[n]
ans = ''
for x in range(i,-1,-1):
    ans = convert(s//(37**x)) + ans
    s -= (37**x)*(s//(37**x))
print(ans)