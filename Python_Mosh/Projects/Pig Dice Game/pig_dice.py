from random import choice
die = (1, 2, 3, 4, 5, 6)

game_end = 30

players = [{'name': 'Player 1', 'score': 0},
           {'name': 'Player 2', 'score': 0}]


def main():

    while players[0]['score'] < game_end or players[1]['score'] < game_end:
        for x in range(2):
            print(f"{players[x]['name']}'s turn")
            while True:
                die_no = choice(die)
                print(f'You rolled a {die_no}')

                if die_no == 1:
                    players[x]['score'] = 0
                    print(f"You scored {players[x]['score']} points this turn")
                    print(
                        f"Current scores: {players[0]['name']}: {players[0]['score']}, {players[1]['name']}: {players[1]['score']}\n")
                    break
                else:
                    players[x]['score'] += die_no
                    roll_again = input('Roll again? (y/n): ').strip().lower()

                if roll_again == 'n':
                    print(f'You scored {players[x]["score"]} this turn')
                    print(
                        f"Current scores: {players[0]['name']}: {players[0]['score']}, {players[1]['name']}: {players[1]['score']}\n")
                    break

    print(f'{players[0]["name"]} wins' if players[0]
          ["score"] >= game_end else f'{players[1]["name"]} wins')


if __name__ == '__main__':
    main()
