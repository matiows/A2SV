col = input()
le = len(col)
sum = 0
for i in range(1, le+1):
    num = ord(col[i-1])-64
    if (le != i):
        sum += num*(26*(le-i))
    else:
        sum += num
print(sum)