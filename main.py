from board_setup import Board
from random import choice
from asciiart import ascii

x_place = []
o_place = []
gb = Board()
clear = "\n" * 100


def check_winner(let):
    for tic_tac_toe in gb.winning_sets:
        if all(x in gb.player[let] for x in tic_tac_toe):
            gb.winner = f"goes to {let}!"
            gb.game_is_on = False
    chars = set('MBLRT')
    if any((c in chars) for c in gb.remaining_choices):
        pass
    else:
        gb.print_board()
        gb.winner = "was a TIE"
        gb.game_is_on = False


def player_go(let):
    print(clear)
    gb.print_board()
    select = input(f"It is {let}'s turn, select a spot:\n "
                   f"{gb.remaining_choices}").upper()
    check = True
    while check:
        if select not in gb.remaining_choices:
            gb.print_board()
            select = input(f"not a valid choice, select again:\n "
                           f"{gb.remaining_choices}").upper()
        else:
            gb.remaining_choices = gb.remaining_choices.replace(f"{select}", "  ")
            check = False
    letters = [a for a in select]
    gb.board[gb.placement[letters[0]]][gb.placement[letters[1]]] = f" {let} "
    gb.player[let].append(select)


def computer_go(let):
    computer_choice = choice(gb.computer_picks)
    check = True
    while check:
        if computer_choice not in gb.remaining_choices:
            computer_choice = choice(gb.computer_picks)
        else:
            gb.remaining_choices = gb.remaining_choices.replace(f"{computer_choice}", "  ")
            check = False
    letters = [a for a in computer_choice]
    gb.board[gb.placement[letters[0]]][gb.placement[letters[1]]] = f" {let} "
    gb.player[let].append(computer_choice)

def game():
    global gb
    global x_place
    global o_place
    print(ascii)
    gb = Board()
    select_game_type = input("One or Two Players:\n").lower()
    if select_game_type == "two" or select_game_type == "2":
        while gb.game_is_on:
            if gb.game_is_on:
                player_go("X")
                check_winner("X")
            if gb.game_is_on:
                player_go("O")
                check_winner("O")
    else:
        computer_turn = choice(["X","O"])
        if computer_turn == "X":
            while gb.game_is_on:
                if gb.game_is_on:
                    computer_go("X")
                    check_winner("X")
                if gb.game_is_on:
                    player_go("O")
                    check_winner("O")
        else:
            while gb.game_is_on:
                if gb.game_is_on:
                    player_go("X")
                    check_winner("X")
                if gb.game_is_on:
                    computer_go("O")
                    check_winner("O")
    print(clear)
    print(ascii)
    print(f"This game {gb.winner}\n")
    replay = input("Would you like to play again? Y/N\n").lower()
    if replay == "y" or replay == "yes":
        print(clear)
        gb.winner=""
        o_place = []
        x_place = []
        gb.game_is_on = True
        game()

game()
