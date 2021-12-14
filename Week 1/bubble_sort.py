def countSwaps(a):
    swap = 0
    for i in range(len(a)):
        for j in range((len(a))-1):
            if a[j]>a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swap=swap+1
    print ("Array is sorted in % s swaps." % swap)
    print ("First Element: % s" % a[0])
    print ("Last Element: % s" % a[(len(a))-1])
