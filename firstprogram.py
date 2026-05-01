age = 21
is_python_easy = True
empty_list= []
numbers = [10,20,30,40]
   
numbers.insert(2,70)

role = "admin"
if role != "admin":
 print("Staff rota access")
else:   
   print("This is not a admin role")

person_tupple = ("Talha",21,"Engineer")

user = {'name': 'talha', 'age':21}

thislist =["Apple","Banana","cherrey","Orange","kiwi","Melon","Mango"]
tropitcal = ["mango", "pineapple", "papaya"]
for newthislist in thislist:
    print(newthislist)
thislist.extend(tropitcal)
print(thislist)
print(thislist[2:3])
print(len(user))
user['gender']= "Male"

# user_key= user.values()
# print(user_key)
# user_name,age,job= person_tupple

# print(f"User name is {user_name}")

# print(f"Age is {age}")

# print(f"job is {job}")


# print(numbers)
# numbers.append(10)
# print(numbers)



# print(first_num)
# if(is_python_easy):
#     print("Yes python is easy")
# else:
#     print("Python is difficult")


# print(f"My age is {age}")