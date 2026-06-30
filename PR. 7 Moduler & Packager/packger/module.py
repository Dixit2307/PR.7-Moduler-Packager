
def module_menu():

    while True:

        print("\n===== EXPLORE MODULE ATTRIBUTES =====")
        print("1. Explore Any Module")
        print("2. Back")

        ch = input("Enter Choice : ")

        if ch == "1":

            name = input("Enter Module Name : ")

            try:

                module = __import__(name)

                print("\nAttributes Available:\n")

                print(dir(module))

            except:

                print("Module Not Found")

        elif ch == "2":
            break