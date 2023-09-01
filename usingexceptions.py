# THIS CODE WILL GENERATE AN ERROR
# x = 10 / 0

# EXCEPTIONS PROVIDE A WAY OF CATCHING ERRORS AND THEN HANDLING THEM
# try:
# x = 10 / 0
# except:
# print("Oops")

# YOU CAN ALSO CATCH SPECIFIC EXCEPTIONS
try:
    answer = input("What should I divide 10 by?")
    num = int(answer)
    print(10 / num)
except ZeroDivisionError as e:
    print("You can not divide it by 0")
except ValueError as e:
    print("You didn't give me a valid number")
    print(e)
finally:
    print("this code always work")
