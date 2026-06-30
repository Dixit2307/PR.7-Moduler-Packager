
import random
import string

def random_menu():

    while True:

        print("\n===== RANDOM DATA GENERATION =====")
        print("1. Generate Random Number")
        print("2. Generate Random Password")
        print("3. Generate Random OTP")
        print("4. Generate Rendom List")
        print("5. Back")

        ch = input("Enter Choice : ")

        if ch == "1":

            print("Random Number =", random.randint(1,100))

            print("\n-----------------------------------------------------")

        elif ch == "2":
            l = int(input("Password Length : "))
            c = string.ascii_letters + string.digits
            password = ""

            for i in range(l):
                password += random.choice(c)

            print("Password =", password)

            print("\n---------------------------------------------------------")

        elif ch == "3":
            print("Random OTP -=-", random.randint(1000,9999))

            print("\n----------------------------------------------------------")
        
        elif ch == "4":
           
           R_list = random.sample(range(1, 101), 5)
           
           print(R_list)

           print("\------------------------------------------------------------")


        
        elif ch =="5": 
            print("\n-----------------------------------------------------------")
            break
        
        else:
            print("Invalid Choice")