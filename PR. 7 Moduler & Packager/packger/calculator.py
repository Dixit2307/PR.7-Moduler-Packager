
def calculator_menu():

    while True:

        print("\n===== CALCULATOR PACKAGE =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Back")

        ch = input("Enter Choice : ")

        if ch in ["1","2","3","4"]:

            a = float(input("Enter First Number : "))
            b = float(input("Enter Second Number : "))

            if ch == "1":
                print("Answer =", a+b)

            elif ch == "2":
                print("Answer =", a-b)

            elif ch == "3":
                print("Answer =", a*b)

            elif ch == "4":
                print("Answer =", a/b)

        elif ch == "5":
            break