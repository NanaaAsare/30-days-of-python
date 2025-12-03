command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("hey, car is already started")
        else:
            started = True
        print(" car started.. ")
    elif command == "stop":
        if not started:
            print("car is already stopped")
        else:
            started = False
        print("car stopped..")
    elif command == "help":
        print("""
start - to the the car 
stop - to stop the car 
quit - to exit the program
        """)
    elif command == "quit":
        break
    else:
        print("sorry i do not understand this message.")