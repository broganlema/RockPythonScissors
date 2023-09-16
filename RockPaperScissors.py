def rock_paper_scissors():
    moves = ["r","p",'s']
    player_1 = input("Player 1: Select (R)ock (P)aper or (S)cissors: ").lower()
    player_2 = input("Player 2: Select (R)ock (P)aper or (S)cissors: ").lower()
    if player_1.lower() and player_2.lower() not in moves:
        print("Your selection was not valid, try again")
        return
    if player_1 == player_2:
        print("TIE")
        return
    elif player_1 =='r' and player_2 =='s' or player_1 =='s' and player_2 =='p' or \
    player_1 =='p' and player_2 =='r':
        print("Player 1 Wins!")
        return
    else:
        print('Player 2 Wins!')
        return
    return
rock_paper_scissors()