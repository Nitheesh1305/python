# P1
'''
while True:
   print("1 : bin")
   print("2 : oct")
   print("3 : hex")
   print("4 : exit")
   choice = int(input("enter your choice:"))
   n = int(input("enter number:"))
   if choice == 1:
      print("Binary of",n,"is",format(n,'b'))
   elif choice == 2:
      print("Octal of",n,"is",format(n,'o'))
   elif choice == 3:
      print("Hexadecimal of",n,"is",format(n,'x'))
   elif choice == 4:
      break
   else:
      print("invalid choice")
      print("run again")

'''
# P2
'''
first_name = input("enter your first name:")
last_name = input("enter your last name:")
print("Hello",first_name,last_name,",welcome to average and percentage calculator application")
sub = int(input("how many subjects do you have : "))
print("Enter marks obtained in %i subjects: "%sub)
total = 0
for i in range(1,sub+1):
   marks = int(input("enter marks in subject%i: "%i))
   total = total + marks
percentage = total/sub
print("Percentage Marks = %0.2f" %percentage)
'''




# P3

while True:
  print("Enter 'x' for exit.")
  num = input("Enter a number: ")
  if num == 'x':
          print("Bye")
          break
  else:
          number = float(num)
          number_sqrt = number ** 0.5
          print("Square Root of %0.3f is %0.3f" %(number, number_sqrt))



# P4
'''
num = int(input("enter number:"))
x = int(input("entered number is divisible by:"))
if num%x == 0:
   print("YES")
else:
   print("NO")
'''


# P5
'''
print("Enter any three numbers: ")
number1 = int(input("Num1: "))
number2 = int(input("Num2: "))
number3 = int(input("Num3: "))
largest = number1
if largest < number2:
     if number2 > number3:
             largest = number2
     else:
             largest = number3
elif largest < number3:
     if number3 > number2:
             largest = number3
     else:
             largest = number2
else:
     largest = number1
print("Largest of given three numbers is",largest)
'''

# P6 Write the programs

# P7
'''
chr() :- convert an ASCII value to it’s corsponding character
>>> chr(97)
'a'
>>> chr(65)
'A'
ord() :- does the opposite of chr.
>>> ord('a')
97
>>> ord("A")
65
'''

# (Print ASCII Values)
'''		
for i in range(1, 255):
     ch = chr(i)
     print(i, "=", ch)
'''


# P8 
'''
nterms = int(input("how many terms?"))
n1=0
n2=1
count=2
if(nterms<=0):
   print("enter a positive number")
elif(nterms==1):
   print("fibonacci:",n1)
else:
   print("fibonacci:")
   print(n1,n2,  end=" ")
   while count<nterms:
      nth = n1+n2
      print(nth, end=" ")
      n1=n2
      n2=nth
      count += 1
'''



# P9
'''	
while True:
     print("Enter 'x' for exit.")
     fah = input("Enter Temperature in Fahrenheit: ")
     if fah == 'x':
             break
     else:
             fahrenheit = float(fah)
             celsius = (fahrenheit-32)/1.8
             print("Temperature in Celsius =",celsius,"\n")

'''


