from random import randint


def end_game():
    print('Game Over.')
    return


def select_words():
    print('\nPicking 3 English 7-letter random words...')
    
    word_list = []
    with open('common-7-letter-words.txt') as txt:
        total_words = txt.read().split('\n')

    for i in range(3):
        random_num = randint(0,len(total_words)-1)
        if len(total_words[random_num]) == 7 and total_words[random_num] not in word_list:
            word_list.append(total_words[random_num])
    
    return word_list
