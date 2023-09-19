seq =list(input("Enter brackets: "))
flag =0
x =0
while x < len(seq):
    #print(x,"-----------", len(seq))
    if seq[x] == '(':
        #print("Found ( ---------->")
        flag =1
        for y in range(x, len(seq)):
            if seq[y] ==')':
                #print("<---------- Found )")
                del seq[y]
                flag =0
                break
    #print(seq)
    x= x+1

if flag == 1 : #not complete
    print("NO")
else:
    print("YES")
