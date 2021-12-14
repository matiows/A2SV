def domino_piling ():
    x, y = [int(x) for x in input().split()]
    return (int((y*x)/2))

print(domino_piling())