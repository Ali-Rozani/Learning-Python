import threading
import time

def Timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1

        print("\nLogged in for",count, "seconds")

x = threading.Thread(target=Timer, daemon=True)
x.start()


Exit = input("Do you wish to exit?")
