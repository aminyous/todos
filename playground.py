# 8 or more
# at least one digit
# at least one capital
# Strong password

answer = "Y"
check_digit = False
check_upper = False

while answer == "Y":

    password = input("Enter new password: ")

    for item in password:
        if item.isdigit():
            check_digit = True
            continue

        if item.isupper():
            check_upper = True

    if len(password) >= 8 and check_digit and check_upper:
        print("Strong Password")
    else:
        print("Weak Password!")

    answer = input("Do you want to retry ? Y/N").capitalize()
    check_digit = False
    check_upper = False

print("*** BYE ***")





















