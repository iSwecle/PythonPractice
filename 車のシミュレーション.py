import time
print("車のシミュレーションへようこそ")
time.sleep(1)
print(input("スタートなら'Enter'をクリックしてください"))
time.sleep(1)
keys = True
motion = False
while True:
    command = input(">")
    if command == "help":
        print("""Commands:
help - shows commands
keys - insert the keys
accele - 
brake""")
    elif command == "keys":
        keys = True
        print("click...*machine noises*")
        command = input(">")
        while keys == True:
            command = input(">")
            if command == "pedal":
                print("broooooooooom...")
                motion = True
                command = input(">")
                while motion == True:
                    command = input(">")
                    if command == "brake":
                        print("thud...stopped.")
                        motion = False
                    else:
                        print("Invalid Action.")
            elif command == "brake":
                print("The car is not even moving yet...")
            elif command == "keys":
                print("*keys removed*")
                keys = False
            else:
                print("Invalid Action.")
    elif command == "brake":
        print("nothing happened...")
    elif command == "pedal":
        print("Insert the keys first")
    else:
        print("Invalid Action.")
