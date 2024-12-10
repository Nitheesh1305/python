# p1
'''
str1 = input("Enter string: ")
print("Modified string:",str1.replace("a","$"))
'''

# p2
'''
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
'''

# p3
'''
name = input("Enter name: ")
cv = 0
cc = 0
cs = 0
for i in name:
    if i in "aeiou":
        cv = cv + 1
    elif i == " ":
        cs = cs + 1    
    else:
        cc = cc + 1
print("Total vowels:",cv)
print("Total consonents:",cc)
print("Number of spaces:",cs)

'''

# p4
'''
str1=input("Enter string: ")
str2=str1.replace(' ','-')
print("Modified string:",str2)
'''

# p5
'''
str1 = input("Enter string:")
count=0
for i in str1:
      count=count+1
print("Length of the string is:")
print(count)
'''

# p6
'''
str1=input("Enter string:")
char=0
word=1
for i in str1:
    if(i==' '):
        word=word+1
    else:
        char=char+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)
'''

# p7
'''
str1=input("Enter string 1: ")
str2=input("Enter string 2: ")

if len(str1)>len(str2):
    print("Length of",str1,"is greater then",str2)

elif len(str1)==len(str2):
    print("Length of",str1,"is eqaul to",str2)

else:
    print("Length of",str1,"is smaller then",str2)

'''

# p8
'''
str1 = input("Enter string:")
sub_str = input("Enter word:")
if(str1.find(sub_str) == -1):
      print("Substring not found in string!")
else:
      print("Substring found in string!")

'''

# p9
'''
str1 = input("Enter String: ")
word = input("Enter Word: ")
list1 = str1.split()
count = 0
for i in range(0,len(list1)):
    if word == list1[i]:
        count = count + 1
print("Count of word is :",count)
'''

# p10
'''
str1 = input("Enter string:")
count1=0
count2=0
for i in str1:
    if(i.isdigit()):
        count1=count1+1
    else:
        count2=count2+1
print("The number of digits is:",count1)
print("The number of characters is:",count2)
'''

















