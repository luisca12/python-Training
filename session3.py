# green = 1
# x = [
#     "red", 
#     "2011",
#     "Ford',
#     green
# ]

# green = True
# x1 = [
#     'red', 
#     2011 
#     'Ford",
#     green
# ]

# green = "green"
# x2 = [
#     "red", 
#     "2011", 
#     "Ford",
#     green
# ]

#################################################

# green = 1
# z = { 
#     "color": 'green'
#     "brand": "Honda", 
# }

# green = True
# z1 = { 
#     'color': green, 
#     "brand": "Honda", 
# }

# green = "green" 
# z2 = { 
#     'color': green 
#     "brand": "Honda", 
# }

#################################################

# showRunTXT = """
# snmp-server community private RO
# snmp-server location LAB-ROUTER-01
# """

# community = ""

# if "private" not in showRunTXT:
#     print("There is a private SNMP Community")
#     community = "private"

#     if "RO" in showRunTXT:
#         print("It's a Read Only SNMP Community")
#         community = community + "-RO"

# elif "public" in showRunTXT:
#     print("There is a public SNMP Community")
#     community = "public"

# else:
#     print("Nothing was found")

# print("The community is:", community)

#################################################
#
#       While   For
#
#################################################

# count = 0

# while count <= 5:
#     print("Count is:", count)
#     count = count + 1
#     # 0 + 1 = 1
#     # 1 + 1 = 2
#     # 2 + 1 = 3
#     # 3 + 1 = 4
#     # 4 + 1 = 5

# print("Count finished, now it's:", count)

# while True:
#     print("Infinite Loop")

# while True:
#     name = input("Please input your name:")
#     lastname = input("Please input your last name:")
#     age = input("Please input your age:")

#     name = str(name)
#     lastname = str(lastname)
#     age = int(age)

#     if age >= 18:
#         print(f"Welcome: {name} {lastname}, you're over 18")
#         print("You may enter")
#         break
#     else:
#         print(f"Welcome: {name} {lastname}, you're not over 18 " \
#               f"You may not enter, current age:{age}")

#################################################

# name = "Luis"
# print(name[3])

#################################################

# totalPages = 10

# for page in range(totalPages):
#     print("Current page is:", page)
 	
# print("All the pages have been saved")

# for page in range(10):
#     print("Current page is:", page)
 	
# print("All the pages have been saved")

# listBooks = [
#     "The Pragmatic Programmer by Andrew Hunt & David Thomas",
#     "Sapiens: A Brief History of Humankind by Yuval Noah Harari",
#     "Clean Code by Robert C. Martin"
# ]

# for book in listBooks:
#     print(f"Currently reading: {book}")

# print("Total amount of books read:", len(listBooks))

#################################################
#
#       Try   Except
#
#################################################
# try:
#     name = input("Please input your name:")
#     age = input("Please input your age:")

#     if age >= 18:
#         print("You may enter") 

# except:
# 	print("Error during age calculation")
	
# except ValueError:
# 	# age = int(input("Please input your age:"))
#     # age = int(age)
#     print("Value error: Age must be a number")
	
# except Exception as error:
# 	print(f"Exception error: {error}")

# except:
# 	print("General Error")
      
#################################################
#
#       Functions
#
#################################################

# def getName():
# 	name = input("What is your name?:")
#   print(f"Your name is: {name}")

# getName()

    ########## ########## ##########

# def getLastName():
# 	lastName = input("What is your last name?:")
# 	return lastName
	
# lastName = getLastName()
# print(f"Your last name is: {lastName}")

    ########## ########## ##########

# def add(a, b):
# 	return a + b

# result = add(1, 2)
# print(f"The sum is: {result}")

    ########## ########## ##########

# def texts(a, b):
# 	return a + b

# result = texts("Luis", "Alfaro")
# print(f"The result is: {result}")

    ########## ########## ##########    

# def defaultValue(textA, textB="Not provided"):
# 	return textA + textB
 	
# result = defaultValue("Luis")
# print(f"The result is: {result}")

    ########## ########## ##########

    # Now we need to build a function that will check the age
# def age(ageNum):
#     if ageNum >= 18:
#         print("You may enter.")
#     else:
#         print("You’re too young.")

# age(18)

    # Now we need to add the try/except

# def age(ageNum):
# 	try:
# 		if ageNum >= 18:
# 			print(f"Age is: {ageNum}, you may enter")
# 		else:
# 			print(f"Age is: {ageNum}, see you next time")
# 	except Exception as error:
# 		 print(f"Error during age calculation: {error} ")

# age(1)

    ########## ########## ##########

# def fullName(name, lastName=""):
# 	getName()
# 	getLastName()
# 	fullname = name + lastName
# 	return fullname
