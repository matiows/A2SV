col = input()
char = []
while col:
    col-=1
    char.append(chr((col%26)+65))
    col//=26
print ("".join( char[::-1]))