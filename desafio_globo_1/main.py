import module
import classes
from random import randint
from time import sleep

if __name__ == "__main__":
    print('Start Game!')
    n_participants = int(input('Enter the number of participants: [2-4] '))
    
    while n_participants not in [2, 3, 4]:
        n_participants = input('Invalid Entry. Do you wish to continue?\n (Type in a number or N)')
        if n_participants.lower() == 'n':
            module.end_game()
    
    print('{} participants will play!'.format(n_participants))

    players = []
    for i in range(n_participants):
        name = input('Give Player {} a name: '.format(i+1))
        players.append(classes.Player(name))
    
    # Select words
    words = module.select_words()
    
    print('\n\nStarting the first round...')
    round = 1
    attempted_letters = set()
    blanks = ('_'*7).strip()
    blanks_list = [blanks, blanks, blanks]
    while True:
        for i in range(n_participants):
            print('{} to play. (Hit "Enter") '.format(players[i].name,i+1))
            print('This play will be worth...')
            sleep(1)
            pts = randint(1,10)
            print(str(pts) + ' points')

            letter = input('\nEnter a letter: ')
            if letter not in attempted_letters:
                attempted_letters.add(letter)
                for word in words:
                    if letter in word:
                        players[i].add_points(pts)
                        for j in range(len(word)):
                            if word[j] == letter:
                                split_answer = list(blanks_list[words.index(word)])
                                split_answer[j] = letter
                                blanks_list[words.index(word)] = ''.join(split_answer)
            else:
                print('Repeated letter.\n')
            print(blanks_list)
    

        print('--- End of round {} ---'.format(round))
        for player in players:
            player.print_score()
        print('---------------------------------\n\n')
        round += 1

        yn = input('Have all words been guessed? (Y/N)')
        while yn.lower() not in ('y', 'n'):
            print('Invalid input.')
            yn = input('Have all words been guessed? (Y/N)')
        
        if yn.lower() == 'y':
            print('Final score.')
            for i in range(n_participants):
                players[i].print_score()
            module.end_game()
