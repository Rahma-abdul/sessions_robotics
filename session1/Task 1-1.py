num = int(input('Enter height: '))
while(num>8):
    num = int(input('Enter height: '))
cnt = num-1
for x in range(1,num+1): #x is the number of levels
    for y in range(cnt,0,-1): #y is the spaces for each level
        print(" ", end ="")
    for z in range(x): #z is the number of hashes of each level
        print("#", end ="")
    print("  ", end="")
    for z in range(x): #z is the number of hashes of each level
        print("#", end ="")
    print("\n", end="")
    cnt = cnt-1
