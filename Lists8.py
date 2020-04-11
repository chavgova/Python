inp = input().split('|')
inp.reverse()
res = []

for s in inp :
    s = s.split()
    res += s

print(*res)
