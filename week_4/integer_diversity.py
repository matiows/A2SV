from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    unique = defaultdict(int)
    for ch in a:
        if unique[ch] == 0:
            unique[ch] = 1
        elif unique[ch*-1] == 0:
            unique[ch*-1] = 1
    print(len(unique))