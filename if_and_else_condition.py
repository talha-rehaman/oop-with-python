age = 25
has_id = True
is_member = False
has_coupon = True

is_banned = False

score = 85
attendence = 90

age = 22
has_id = True
is_vip = False
ticket_price = 50

if (age >= 21 and has_id) or is_vip:
    print("Welcome to the club!")
    if ticket_price > 30 and (age < 25 or is_vip):
        print("You get a 20% student discount!")
    else:
        print("Regular price applies")
else:
    print("Sorry, cannot enter")

# is_raining= False
# if not is_raining:
#     print("Lets go for a walk")
# else:
#     print("Better stay inside")
# if score > 80 and attendence > 85:
#   print("Excellent Student")
# else:
#   print("Need Improvement")


# if not is_banned:

#     print("Welcome!") 
# if is_member or has_coupon:
#     print("Discount Applied")
# else:
#     print("No discount")
# if age < 30 and has_id:
    # print("You can drive!")
# else:
    # print("You cannot drive.")
