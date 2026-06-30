
def file_menu():

    while True:

        print("\n===== FILE OPERATIONS =====")
        print("1. Read Sample.txt")
        print("2. Write Sample.txt")
        print("3. Write Log.txt")
        print("4. Read Log.txt")
        print("5. Create new file")
        print("6. Back")
        print("\n--------------------------------")

        ch = input("Enter Choice : ")

        if ch == "1":
            file = open("Data/sample.txt","r")

            print(file.read())

            file.close()

            print("\n-----------------------------------------------------")

        elif ch =="2":
            file = open("Data/sample.txt","a")

            file.write(text + "\n")

            file.close()

            print("Sample Saved Successfully")

            print("\n------------------------------------------------------")

        elif ch == "3":
            text = input("Enter Log Message : ")

            file = open("Data/log.txt","a")

            file.write(text + "\n")

            file.close()

            print("Log Saved Successfully")

            print("\n------------------------------------------------------")

        elif ch == "4":
            file = open("Data/Log.txt","r")

            print(file.read())

            file.close()

            print("\n-------------------------------------------------------")
        
        elif ch == "5":
             File = str(input("Enter File Name for creat file :"))
            
             file = open(File,"w")
             file.write("New File")
             file.close()

             print("File Created Successfully.")

             print("\n--------------------------------------------------------")

        elif ch == "6":
            print("/n----------------------------------------------------------")
            break

        else:
            print("Invalid Choice")