#Working with print function and their techniques
'''print("I")
print("Learn")
print("Python")

print('I' , 'Learn' , 'Python')

print('I' , 'Learn' , 'Python' , sep='$$')

print("I" , end=" ")
print("Learn" , end=" ")
print("Python")

print("Using multiple print statements:")
print("*")
print("**")
print("***")

print("Using single print statement:")
print("""*
**
***""")

print("Using escape sequence:")
print("*\n**\n***\n")'''

#Building a calculator in python
'''print("Calculator in python")
a = float(input("A: Enter a Digit: "))
b = float(input("B: Enter a Digit: "))
sign = input("Enter What you want to do with these numbers: ")
if sign == "+":
    add = a+b
    print("A+B: " , add)
elif sign == "-":
    diff =  a-b
    print("A-B: " , diff)
elif sign == "*":
    mult = a*b
    print("A*B: " , mult)
elif sign == "/":
    div = a/b
    print("A/B: " , div)
elif sign == "//":
    floordiv == a//b
    print("A//B: " , floordiv)
elif sign == "%":
    mod = a%b
    print("A%B: " , mod)
elif sign == "**":
    e = int(input("Enter a exponentiation power: "))
    base_selector = input("Select what you want as Base A or B: ")
    if base_selector == "a":
        print("Your value is: " , a**e)
    else:
        print("Your value is: " , b**e)'''

#identifying and evaluating the string
'''charact = input("Enter a single character: ")
if ord(charact) > 47 and ord(charact) < 58:
    print(charact , "is a number")
elif ord(charact) > 64 and ord(charact) <91:
    print(charact , "is a uppercase alphabet")
elif ord(charact) > 96 and ord(charact) < 123:
    print(charact , "is a lowercase alphabet")
else:
    print(charact , "is a special character")'''

#identifying and evaluating the numbers
'''num = float(input("Enter a number: "))
if num > 0:
    print(num , "is a positive number")
elif num < 0:
    print(num , "is a negative number")
elif num == 0:
    print(num , "is zero")
else:
    print("Enter a number first")

num = float(input("Enter a number: "))
if num == 0:
    print(num , "is neither even nor odd")
elif num % 2 == 0:
    print(num , "is even")
elif num % 2 != 0:
    print(num , "is odd")
else:
    print("Enter a number first")'''

#Write a program to count the number of words in a given string

'''string = input("Enter  a string: ")
string_ =  string+" "
cnt = 0
for i in string_:
    if i == " ":
        cnt = cnt + 1
print(cnt)'''

#Write a program to count the numbers of alphabets, digits and special characters from the given string

'''string = input("Enter a string to count its alphabets, digits and special characters: ")
cnt_a=cnt_d=cnt_s=cnt=0
for i in string:
    cnt = cnt +1
    if i.isalpha():
        cnt_a = cnt_a + 1
    elif i.isdigit():
        cnt_d = cnt_d+1
    else:
        cnt_s = cnt_s + 1
print("Total length of the string: ", cnt)
print("Number of alphabets in the string: ", cnt_a)
print("Number of digits in the string: ", cnt_d)
print("Number of special characters in the given string: ", cnt_s)'''

#To display the occurence of words starting with a vowel in the given string

'''string = input("Enter a string: ")
string_ = string.split()
vowels = "aeiouAEIOU"
cnt = 0
for i in string_:
    for j in vowels:
        if i.startswith(j):
            cnt = cnt + 1
print(cnt)'''

#To replace all the vowels in the given string with X

'''string = input("Enter a string to change its vowel with 'X' : ")
ch = ""
for i in string:
    if i in "AEIOUaeiou":
        ch = ch + "X"
    else:
        ch = ch+i
print(ch)'''

#Write a program which reverses a string without using slicing & stores the reversed string in a new string

'''string = input("Enter a string to reverse without using slicing method: ")
lstring = len(string)
rstring = ""
for i in range(lstring-1,-1,-1):
    rstring = rstring + string[i]
print(rstring)'''

#Write a program to input a line of text and print the biggest word from it

'''string = input("Enter a sentence to print the biggest word from it: ")
s_string = string.split()
nstring = ""
for i in s_string:
    if len(i) > len(nstring):
        nstring = i
print(nstring)'''

#Write a program to check whether the given string is palindrome or not

'''string = input("Enter a string: ").lower()
rstring = string[::-1]
if string == rstring:
    print("The given string is a Palindrome")
else:
    print("The given string is not a Palindrome")'''

#To read a line of text that counts the word "is" apprearce in the line and display its count

'''string = input("Enter a line of text: ")
print("The number of times the 'is' apprearing on the given string is: ",string.count("is"))'''

#To count the number of vowels in a given string

'''string = input("Enter a string to count the number of times a vowel appearing in the given string : ")
cnt = 0
for i in string:
    if i in "AEIOUaeiou":
        cnt += 1
    else:
        continue
print("Number of times vowels appearing: ",cnt)'''

#Input a string with many words along with a space between each word and replace each space with a hyphen

'''string = input("Enter a sentence to replace the spaces with hyphen: ")
string_new = string.replace(" ","-")
print("The new string is: ", string_new)'''

#Using python to create a flames calculator

'''name_1 = input("Enter your name: ").replace(" ","").upper()
name_2 = input("Enter another name: ").replace(" ","").upper()
name_lis1 = list(name_1)
name_lis2 = list(name_2)
for i in name_1:
    if i in name_2:
        name_lis1.remove(i)
        name_lis2.remove(i)
    else:
        continue
final = name_lis1 + name_lis2
output = len(final)
dicti = {1:"S",2:"E",3:"F",4:"E",5:"F",6:"M",7:"E",8:"A",9:"S",10:"L",11:"M",12:"A",13:"A",14:"F",15:"M"}
dictii = {"F":"Family","L":"Love","A":"Affection","M":"Marriage","E":"Enemies","S":"Siblings"}
print(dictii[dicti[output]])'''

#To create a list dynamically using for loop

'''lis=[]
while True:
    inp=input("Enter elements to place them in a list otherwise press enter: ")
    if inp == "":
        break
    else:
        lis.append(inp)    
print(lis)'''

#Create a list using for loop that contains integer from 0 to 49

'''print("Welcome!!")
lis=[]
for i in range(1,50,1):
    lis.append(i)
print(lis)'''

#Create a list using for loop that contains the square of integers from 1 to 20

'''lis=[]
j = 0
for i in range(1,21,1):
    j = i**2
    lis.append(j)
print(lis)'''

#Create a integer list using for loop and check the number from the user is present in the lis or not if the number is present display the index of that number or display an appropriate message 

'''import random
n = int(input("n: Enter the range of the list starting from 1 to n: "))
lis = []
if n == 1:
    print("katham bye bye tata goodbye gaya")
elif n != 1:
    for i in range(1,n+1,random.randint(1,n-1)):
        lis.append(i)
        random.shuffle(lis)
    inp = int(input("Enter your Guess: "))
    if inp == 1:
        print("You found an loophole didn't you ;) ")
    if inp in lis:
        print("index of the number",lis.index(inp))
    else:
        print("I'm afraid that I can't find your element here :( ")'''

#To display the unique and duplicate items of a given list into two different list

'''lis=eval(input("Enter a list: "))
lis1 = lis.copy()
sil_ori = []; sil_dupli = []
for i in lis:
    if lis1.count(i) == 1:
        sil_ori.append(i)
    elif lis1.count(i) > 1:
        sil_dupli.append(i)
        lis1.remove(i)
        l=lis.index(i)
        try:
            lis1.pop(l)
        except:
            continue    
    else:
        continue    
print("Original elements: ",sil_ori)
print("Duplicate elements: ",sil_dupli)'''

#To display a square of an element if it is a integer and change the case if the element is string by considering that the list l contains both number and string as it's elements 

'''lis = eval(input("Enter a list containing only strings and numbers: \n"))
l = []
for i in lis:
    if i == str(i):
        if i.isalpha():
            l.append(i.swapcase())
    else:
        l.append(i**2)        
print(l)'''