# p1

list1=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    list1.append(b)
list1.sort()
print("Second largest element is:",list1[n-2])













# p2
'''
list1=[]
even = []
odd = []
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    list1.append(b)
for i in list1:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

print("Even List :",even)
print("Odd List :",odd)
'''

# p3
'''
list1=[]
list2=[]
n1=int(input("Enter number of elements for list 1:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    list1.append(b)
n2=int(input("Enter number of elements for list 2:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    list2.append(d)
new=(list1 + list2)
new.sort()
print("Sorted list is:",new)
'''

# p4
'''
n=int(input("Enter the lower range:"))
m=int(input("Enter the upper range:"))
list1 = []
for i in range(n,m+1):
    list1.append((i,i**2))

print(list1)
'''
##same program using list comprehension    
##list1=[(i,i**2) for i in range(n,m+1)]













