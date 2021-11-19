from art import art
import random

board_dic = {'1': ' ', '2': ' ', '3': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '7': ' ', '8': ' ', '9': ' '}


def board_display(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('- + - + -')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('- + - + -')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])


def check_winner(player):
    win_txt = f'\nPlayer {player} won 👏👏👏\nGame Over!'
    if board_dic['1'] == board_dic['2'] == board_dic['3'] != ' ':
        print(win_txt)
        return True
    elif board_dic['4'] == board_dic['5'] == board_dic['6'] != ' ':
        print(win_txt)
        return True
    elif board_dic['7'] == board_dic['8'] == board_dic['9'] != ' ':
        print(win_txt)
        return True
    elif board_dic['1'] == board_dic['4'] == board_dic['7'] != ' ':
        print(win_txt)
        return True
    elif board_dic['2'] == board_dic['5'] == board_dic['8'] != ' ':
        print(win_txt)
        return True
    elif board_dic['3'] == board_dic['6'] == board_dic['9'] != ' ':
        print(win_txt)
        return True
    elif board_dic['1'] == board_dic['5'] == board_dic['9'] != ' ':
        print(win_txt)
        return True
    elif board_dic['3'] == board_dic['5'] == board_dic['7'] != ' ':
        print(win_txt)
        return True


def first_player():
    return random.randint(1, 2)


def swap_players(player):
    if player == 'O':
        return 'X'
    else:
        return 'O'


def play_game():
    print(art)
    num_of_moves = 0
    all_players_input = []
    game_over = False

    if first_player() == 1:
        player = 'X'
    else:
        player = 'O'

    while not game_over:
        player_input = input(f'\nPlayer_{player}: ')
        if player_input in all_players_input:
            print('This cell is busy, try another one.')
            continue
        elif player_input not in board_dic.keys():
            print('Only numbers from 1 to 9 allowed. Please try again.')
            continue
        num_of_moves += 1
        all_players_input.append(player_input)
        board_dic[player_input] = player
        board_display(board_dic)
        if check_winner(player):
            game_over = True

        if num_of_moves == 9 and not check_winner(player):
            print('Game Draw! 🙃')
            game_over = True
        player = swap_players(player)


while input("\nDo you want to play a game of TiTacToe? Type 'y' or 'n': ") == "y":
    for key in board_dic.keys():
        board_dic[key] = ' '
    play_game()
