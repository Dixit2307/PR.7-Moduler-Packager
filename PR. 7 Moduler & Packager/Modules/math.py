
import math

def math_menu():

    while True:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("\n===== MATHEMATICAL OPERATIONS =====")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

        print("\n1. Factorial")
        print("2. Compound Interest")
        print("3. Trigonometric Functions")
        print("4. Area of Geometric Shapes")
        print("5. Back")

        ch = input("Enter Choice : ")

        if ch == "1":
            import math

            num = int(input("Enter Number : "))

            N = math.factorial(num)

            print("Factorial =",N)

            print("\n----------------------------------------------------------")

        elif ch == "2":

            p = float(input("Principal Amount : "))
            r = float(input("Rate (%) : "))
            t = float(input("Time (Years) : "))

            amount = p * ((1 + r/100) ** t)

            print("Amount =", round(amount,2))

            print("\n---------------------------------------------------------------")

        elif ch == "3":

            angle = float(input("Enter Angle : "))

            print("Sin =", round(math.sin(math.radians(angle)),4))
            print("Cos =", round(math.cos(math.radians(angle)),4))
            print("Tan =", round(math.tan(math.radians(angle)),4))

            print("\n----------------------------------------------------------------")
        
        elif ch == "4":
            while True:
                print("/n Whice Shapes Area You have to Find :")
                print("1. Circle")
                print("2. Square")
                print("3. Rectengle")
                print("4. Back")
                print("\n-------------------------------------")

                A =input("Enter your choice : ")

                if A == "1":
                    import math
                    radius = float(input("Enter radius of circle :"))

                    area = math.pi * (radius ** 2)
                    print("Area of circle :", area)

                    print("\n-----------------------------------------------------")
                
                elif A == "2":
                    side = float(input("Enter Side of square :"))
                    area = side ** 2

                    print("Area of Square :",area)

                    print("\n------------------------------------------------------")
                
                elif A == "3":
                    l = float(input("Enter the length of the rectangle: "))
                    w = float(input("Enter the width of the rectangle: "))

                    area = l * w
                    print("Area of Rectengle  :",area)

                    print("\n-------------------------------------------------------")
                
                elif A == "4":
                    break

                else:
                    print("Inavlid Inpute By the user")
            
        elif ch == "5":
            print("\n---------------------------------------------------------------")
            break

        else:
            print("Invalid Choice")