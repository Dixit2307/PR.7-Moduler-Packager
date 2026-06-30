from datetime import datetime, timedelta
import time

def datetime_menu():

    while True:

        print("\n===== DATETIME OPERATIONS =====")
        print("1. Current Date and Time")
        print("2. Difference Between Dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back")

        ch = input("Enter Choice : ")

        if ch == "1":
            print("\nCurrent Date & Time")
            print(datetime.now())

        elif ch == "2":
            d1 = input("Enter First Date (YYYY-MM-DD) : ")
            d2 = input("Enter Second Date (YYYY-MM-DD) : ")

            date1 = datetime.strptime(d1, "%Y-%m-%d")
            date2 = datetime.strptime(d2, "%Y-%m-%d")

            diff = abs((date2 - date1).days)
            print("Difference =", diff, "Days")

        elif ch == "3":
            now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            print(now)

        elif ch == "4":
            T = int(input("Enter how long you want the stopwatch to run (seconds): "))
            start_time = datetime.now()
            print("Stopwatch started...")

            time.sleep(T)

            end_time = datetime.now()
            elapsed = end_time - start_time
            print(f"Elapsed time: {elapsed}")

        elif ch == "5":
            
            sec = int(input("Enter seconds for countdown: "))
            dur = timedelta(seconds=sec)
            end_time = datetime.now() + dur
            print("Countdown started...")

            while datetime.now() < end_time:
                remaining = end_time - datetime.now()
                print(f"Time left: {remaining}", end="\r")
                time.sleep(0.1)

            print("\nTime is up!")

        elif ch == "6":
            break

        else:
            print("Invalid Choice")