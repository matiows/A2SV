s = input()
sum = 0
for i in range(len(s)):
    if s[i] == 'M':
        sum+= 1000
    elif s[i] == 'D':
        sum+= 500
    elif s[i] == 'C':
        sum+= 100
    elif s[i] == 'L':
        sum+= 50
    elif s[i] == 'X':
        if i != 0 and s[i-1] == 'I':
            sum+= 8
        else:
            sum+= 10
    elif s[i] == 'V':
        if i != 0 and s[i-1] == 'I':
            sum+= 3
        else:
            sum+= 5
    elif s[i] == 'I':
        sum+= 1
print(sum)