n=input()
for i in range(1,n+1):
    print (" "*(n-i), end="")
    print (int('1'*(i))**2)
for i in range(n,1,-1):
    print (" "*((n+1)-i), end="")
    print (int('1'*(i-1))**2)