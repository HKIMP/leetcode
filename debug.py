res = []

n = int(input())

for _ in range(n):
    s = input()
    if s != '':
        tmp = [j for j in s.split()]
        res.append(tmp[0])
    else:
        break
print(res)