# Using While loop


# def main():
# x = 0

# while x < 5:
# print(x)
# x = x + 1


# main()

# For Loop
# for x in range(5, 10):
# print(x)
#
# main()

# using for loop for a collection
# days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# for d in days:
# print(d)

# Use the break and continue statement
for x in range(5, 10):
    if x == 7:
        break
    if x % 2 == 0:
        continue
    print(x)

# using enumerate function() to get index
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i, d in enumerate(days):
    print(i, d)
