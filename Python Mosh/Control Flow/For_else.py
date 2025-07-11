successful = False

for number in range(3):
    print('Attempt')

    if successful:
        print('Successful')
        break  # to leave a loop

else:    # Executes if the for loop completes normally without encountering a break
    print('Attempted 3 times and failed')
