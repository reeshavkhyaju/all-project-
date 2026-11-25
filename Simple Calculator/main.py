# print("Python Calculator")

# print("=" * 20)

# print()

# # num1 = input("Enter the first number: ")
# # num2 = input("Enter the second number: ")

# # print("You entered:", num1, num2)

# # print(num1 + num2)

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# # result = num1 + num2
# # print(result)

# operator = input("Enter an operation (+, -, *, /, **): ")

# print("You chose:", operator)

# if operator == '+':
#     result = num1 + num2
#     print(result)

# elif operator == '-':
#     result = num1 - num2
#     print(result)

# elif operator == '*':
#     result = num1 * num2
#     print(result)

# elif operator == '**':
#     result = num1 ** num2
#     print(result)

# elif operator == '/' and num2 != 0:
#     result = num1 / num2
#     print(result)
# elif operator == '/' and num2 == 0:
#     print("Cannot divide by Zero!")

# else:
#     print("Invalid Operator!")

# while True:
#     print("Python Calculator")
#     print("=" * 20)
#     print()

#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))

#     operator = input("Enter an operation (+, -, *, /, **): ")
#     print("You chose:", operator)

#     if operator == '+':
#         result = num1 + num2
#         print(f"{num1} + {num2} = {result}")
#     elif operator == '-':
#         result = num1 - num2
#         print(f"{num1} - {num2} = {result}")
#     elif operator == '*':
#         result = num1 * num2
#         print(f"{num1} * {num2} = {result}")
#     elif operator == '**':
#         result = num1 ** num2
#         print(f"{num1} ** {num2} = {result}")
#     elif operator == '/' and num2 != 0:
#         result = num1 / num2
#         print(f"{num1} / {num2} = {result}")
#     elif operator == '/' and num2 == 0:
#         print("Cannot divide by Zero!")
#     else:
#         print("Invalid Operator!")

#     reset = input("Press 'C' to calculate again. Press any other key to exit! ")

#     # if reset.lower() != "c":
#     #     break

#     # if reset not in ("C", "c"):
#     #     break

#     if reset not in ("C", "c"):
#         print("GOODBYE!")
#         break



while True:
    print()
    print("Python Calculator")
    print("=" * 20)
    print()

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    operator = input("Enter an operation (+, -, *, /, **): ")
    print("You chose:", operator)
    print()

    if operator == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operator == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operator == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operator == '**':
        result = num1 ** num2
        print(f"{num1} ** {num2} = {result}")
    elif operator == '/' and num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    elif operator == '/' and num2 == 0:
        print("Cannot divide by Zero!")
    else:
        print("Invalid Operator!")

    print()

    reset = input("Press 'C' to calculate again. Press any other key to exit! ")

    if reset not in ("C", "c"):
        print("GOODBYE!")
        print()
        break