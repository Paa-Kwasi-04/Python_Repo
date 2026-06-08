
while True:
    command = input('>')
    print("ECHO", command)
    if command.lower() == 'quit':  # helps you break from the infinite loop
        break
