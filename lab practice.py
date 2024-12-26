#question 01, Write a program that will check the given string is palindrome word or not.

# def is_palindrome(word):
#     word1 = word.replace(" ", "").lower()
#     reverse = word1[::-1]
#     return word1 == reverse


# word1 = "Mom"
# print(f"{is_palindrome(word1)}")

# #question 2, write a program that returns the minimum of three number using if...elif..else.

# def find_minimum(a, b, c):
#     if a <= b and a <= c:
#         return a
#     elif b <= a and b <= c:
#         return b
#     else:
#         return c

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))

# minimum = find_minimum(num1, num2, num3)
# print(f"The minimum of the three numbers is: {minimum}")

# #question 3, write a program that accept four digit numbers and find the last two digit of number accepted from user is divisible by 3.

# number = input("Enter a four-digit number: ")
# if len(number) == 4 :
#     last_two_digits = int(number[-2:])
#     if last_two_digits % 3 == 0:
#         print(f"The last two digits ({last_two_digits}) are divisible by 3.")
#     else:
#         print(f"The last two digits ({last_two_digits}) are not divisible by 3.")
# else:
#     print("Invalid input! Please enter a valid four-digit number.")

# #question 4, write a program that remove n character from the end of given string.

# string = input("Enter a string: ")
# n = int(input("Enter the number of characters to remove from the end: "))
# if n < 0:
#     print("The number of characters to remove cannot be negative.")
# elif n > len(string):
#     print("The number of characters to remove exceeds the string length.")
# else:
#     newstring = string[:-n]
#     print(f"The modified string is: {newstring}")

#question5, write a program accept a string from the user and dispaly characters present at an odd index number.
# #question6, write a program that accept two numbers and perform given arthmetic opreation is the numbers using match.

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# print("Choose an arithmetic operation:")
# print("+")
# print("-")
# print("*")
# print("/")

# operation = input("Enter the operation (+, -, *, /): ")

# match operation:
#     case "+":
#         result = num1 + num2
#         print(f"The result of addition is: {result}")
#     case "-":
#         result = num1 - num2
#         print(f"The result of subtraction is: {result}")
#     case "*":
#         result = num1 * num2
#         print(f"The result of multiplication is: {result}")
#     case "/":
#         if num2 != 0:
#             result = num1 / num2
#             print(f"The result of division is: {result}")
#         else:
#             print("Error: Division by zero is not allowed.")
#     case _:
#         print("Invalid operation selected.")


# num1=int(input("enter number 1"))
# num2=int(input("enter number 2"))

# oprator=input("enter oprator(+,/,*,-):")
# match oprator:
#      case '+':
#          print(num1+num2)
#      case '-':
#           print(num1-num2)
#      case '/':
#            print(num1/num2)
#      case  '*':
#         print(num1*num2)
#      case _:
#         print("it is not arthimetic")


# #in the acepted string check the STRING and lastly write like this "localization = (l10n)" but it works for only if the len of char is morethan 10 char.

# string = input("Enter a string: ")

# if len(string) > 10:
    
#     shorthand = f"{string[0]}{len(string)-2}{string[-1]}"
#     result = f"{string} = ({shorthand})"
#     print(result)
# else:
#     print("The string length is not greater than 10.")
