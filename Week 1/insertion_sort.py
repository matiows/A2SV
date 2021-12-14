def insertionSort1(a):
    for i in reversed(range(len(a))):
        temp = a[i]
        for j in reversed(range(i+1)):
            if a[j]>temp:
                a[j+1]=a[j]
                print(' '.join(map(str, a))) 
                if j==0:
                    a[j]=temp
            elif a[j]<temp:
                a[j+1]=temp
                break
    print(' '.join(map(str, a))) 
                
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(arr)

