from Modules.datetime import datetime_menu
from Modules.math import math_menu
from Modules.random import random_menu
from Modules.uuid import uuid_menu
from Modules.file import file_menu

from packger.module import module_menu

while True:
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("\n===== MULTI UTILITY TOOLKIT =====")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

    print("1. Date & Time")
    print("2. Mathematics")
    print("3. Random Generator")
    print("4. UUID Generator")
    print("5. File Handling")
    print("6. Module Explorer")
    print("7. Exit")
    print("====================================")

    choice = input("Enter Choice : ")

    if choice == "1":
        datetime_menu()

    elif choice == "2":
        math_menu()

    elif choice == "3":
        random_menu()

    elif choice == "4":
        uuid_menu()

    elif choice == "5":
        file_menu()
        
    elif choice == "6":
        module_menu()

    elif choice == "7":
        print("Thank You")
        break

    else:
        print("Invalid Choice")

