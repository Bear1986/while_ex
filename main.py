import random

# for num in range(1,11, 1):
#  print(num)

# print()

# #how to create a while loop
#Remember Start, Stop, Step

num = 1    ##Start## declare the value  
while num < 11:    ##Stop## while num less then but not = to 11: 
  print(num)    #print num and incrment it by
  num += 1    ##Step## 1 untill it's 10 


# print()

# # some examples below of while loops with strings and useing inputs

# copy = input("What did you say? ")
# while copy != "stop": #sentinal value
#   print(copy + " ")
#   copy = input("What did you say? ")

# print()

# num = eval(input("Whats your fav num? "))
# while num != 7: #
#   print("try again!")
#   num = eval(input("Whats your fav num? "))

# print()

# msg = input("whats the password? ")
# while msg != "please":
#   print("wrong")
#   msg = input("whats the password? ")

# print()


# msg = input("Say something: ")

# while msg != "stop":
#   msg = input(f"{msg}\n")
# print("you win!!!")

# num = int(input("How many times should I tell you?: "))
# mes = input("What should I tell you?: ")

# for num in range(num):
#   print(mes)
#   if num >= 3:
#     print("Please!!!")
#     break

# print()

# turn these into while loops

# x_random = random.randint(0, 10)

# print(f"The random number taken is: {x_random}")

# for x in range(11):
#   if not x == x_random:
#     print(x)

# print()

# x_random = random.randint(0, 15)
# print(x_random)

# print()

# if x_random < 10:
#  for i in range(10, 16):
#    print(i)


# print()

# user_int = int(input("Enter a whole number please:\n "))

# while user_int != 7:
#   print("Try again")
#   user_int = int(input("Enter a whole number please:\n "))
# print("7 is the best number")