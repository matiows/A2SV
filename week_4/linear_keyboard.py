t = int(input())
for _ in range (int(t)):
    keyboard = input()
    s = input()
    key_dic = {}
    sum = 0
    for i in range(1,len(keyboard)+1):
        key_dic[keyboard[i-1]] = i
    for i in range(len(s)-1):
        sum+=abs(key_dic[s[i]] - key_dic[s[i+1]])
    print (sum)