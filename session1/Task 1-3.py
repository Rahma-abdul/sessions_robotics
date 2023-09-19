from math import floor

money = int(input("input: "))
two_hundreds = floor(money/200)
if two_hundreds != 0:
    print(two_hundreds,"x 200 L.E.",end = " ")
    money = money-200 *two_hundreds

one_hundreds = floor(money/100)
if one_hundreds != 0:
    if two_hundreds != 0:
        print("+ ",one_hundreds,"x 100 L.E.",end = " ")
    else:
        print(one_hundreds, "x 100 L.E.", end=" ")
    money = money-100 *one_hundreds

fifties = floor(money/50)
if fifties != 0:
    if two_hundreds != 0 or  one_hundreds !=0:
        print("+ ",fifties,"x 50 L.E.",end = " ")
    else:
        print(fifties, "x 50 L.E.", end=" ")
    money = money-50 *fifties

twenties = floor(money/20)
if twenties != 0:
    if two_hundreds!=0 or one_hundreds!=0 or fifties!=0:
        print("+ ",twenties, "x 20 L.E.", end=" ")
    else:
        print(twenties,"x 20 L.E.",end = " ")
    money = money-20 *twenties

tens = floor(money/10)
if tens != 0:
    if two_hundreds!=0 or one_hundreds!=0 or fifties!=0 or twenties!=0:
        print("+ ",tens,"x 10 L.E.",end = " ")
    else:
        print(tens,"x 10 L.E.",end = " ")
    money = money-10 *tens

fives = floor(money/5)
if fives != 0:
    if two_hundreds!=0 or one_hundreds!=0 or fifties!=0 or twenties!=0 or tens !=0:
        print("+ ",fives,"x 5 L.E.",end = " ")
    else:
        print(fives,"x 5 L.E.",end = " ")
    money = money-5 *fives

ones = floor(money)
if ones != 0:
    if two_hundreds!=0 or one_hundreds!=0 or fifties!=0 or twenties!=0 or tens !=0 or fives!=0:
        print("+ ",ones,"x 1 L.E.")
    else:
        print(ones,"x 1 L.E.")
    money = money-1 *ones




