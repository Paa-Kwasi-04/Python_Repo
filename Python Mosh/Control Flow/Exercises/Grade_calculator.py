while True:
    Score = int(input('Enter your score> '))

    if Score <= 100:

        if 100 >= Score >= 90:
            print('Grade A')
        elif 90 > Score >= 80:
            print('Grade B')
        elif 80 > Score >= 70:
            print('Grade C')
        elif 70 > Score >= 60:
            print('Grade D')
        else:
            print('Grade F')
    else:
        print(f'{Score} is an invalid Score')
        break
