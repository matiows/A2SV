n=input()
for i in range(1,n+1):
    print ("*"*(i), end="")
    print (" "*((n-i)*2),end="")
    print ("*"*(i))