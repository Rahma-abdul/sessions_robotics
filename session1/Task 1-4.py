card = int(input("input: "))
card2 =int(card/10)
card3 = card
sum1 =0
sum2 =0
while card != 0:
    digit = card %10
    card = int(card / 100)
    sum1 = sum1 +digit
#print(sum1)
while card2 != 0:
    digit = card2 % 10
    card2= int(card2 / 100)
    digit = digit*2
    #print(digit)
    if digit>9:
        x = digit % 10
        sum2 = sum2+x+int(digit/10)
        #print(sum2, "sum2<----------")
    else:
        sum2 = sum2 + digit
        #print(sum2, "sum2<----------")
#print(sum2)
total = sum1+sum2
#print(total)
if total%10 == 0:
    x1 = int(str(card3)[:1])
    x2 = int(str(card3)[1:2])
    if x1 == 4 :
        print("Visa")
    elif x1 == 3 and (x2 == 4 or x2 == 7):
        print("American Express")
    #elif x1 == 5 and (x2 == 1 or x2 == 2 or x2 == 3 or x2 ==4 or x2 == 5):
    else:
        print("MasterCard")

else:
    print("Invalid")