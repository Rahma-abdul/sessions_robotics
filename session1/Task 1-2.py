txt = input("input: ")
special = txt.count('.') + txt.count('!') + txt.count('?') + txt.count(' ') + txt.count('\'') + txt.count('%') + txt.count('&') + txt.count('*') + txt.count('^') + txt.count('$') +txt.count('(') + txt.count(')') + txt.count(',')
#print(special)
letters = len(txt) - special
#print(letters)
sen = txt.count('.') + txt.count('!') + txt.count('?')
#print(sen)
words = len(txt.split())
#print(words)
l =letters/words *100
#print(l)
s = sen/words *100
#print(s)
grade = round(0.0588 * l- 0.296 * s - 15.8)
if(grade >= 16):
    print("Grade: 16+")
elif (grade< 1):
    print("Before grade 1")
else:
    print("Grade:",grade)
#One fish. Two fish. Red fish. Blue fish. (Before Grade 1)
#Would you like them here or there? I would not like them here or there. I would not like them anywhere. (Grade 2)
#In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since. (Grade 7)
#There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy. (Grade 9)
#A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains. (Grade 16+)