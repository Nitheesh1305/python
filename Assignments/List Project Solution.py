# List Project

list1 = []
list2 = []
list3 = []
str1 = "CRM SOFTWARE"
print("\n",str1.center((len(str1)+40),"*"),"\n")
while True:
   print("1: ADD DATA".rjust(21))
   print("2: SHOW DATA".rjust(22))
   print("3: DELETE DATA".rjust(24),"\n")
   
   choice = int(input("enter your choice : "))
   
   if choice == 1:
      print("".center(30,"-"))
      name1 = input("enter your name : ")
      list1.append(name1)
      age1 = input("enter your age : ")
      list2.append(age1)
      phone1 = input("enter your phone number : ")
      list3.append(phone1)
      print('\n')
      print("Data added".center(40,"_"),"\n")
      
      ch = input("press c for continue and x for exit : ")
      print("".center(30,"-"))
      if ch == "c":
         pass
      elif ch == "x":
         break

   elif choice == 2:
      print("".center(30,"-"))
      name2 = input("enter name you want to search: ")
      if name2 in list1:
         print("record found".center(40,"_"),"\n")
         get_index = list1.index(name2)
         print("".center(30,"-"))
         print("Name : {}\nAge : {}\nPhone number : {}".format(list1[get_index],list2[get_index],list3[get_index]))
         print("".center(30,"-"),"\n")

         ch = input("press c for continue and x for exit : ")
         print("".center(30,"-"))
         if ch == "c":
            pass
         elif ch == "x":
            break
      else:
         print("not found")
   
   elif choice == 3:
      print("".center(30,"-"),"\n")
      name3 = input("enter name you want to delete: ")
      if name3 in list1:
         print("record found")
         print("deleting record.............")
         get_index = list1.index(name3)
         del list1[get_index]
         del list2[get_index]
         del list3[get_index]
         print("\n%s deleted"%name3,'\n')
         print("".center(30,"-"),"\n")

         ch = input("press c for continue and x for exit : ")
         print("".center(30,"-"))
         if ch == "c":
            pass
         elif ch == "x":
            break
      else:
         print("not found")
         
   else:
      print("invalid input")
