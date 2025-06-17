
#Utilis for game_controller

def clear_console():
    import os
    os.system('cls')

def toggle_xy(current_player):
    if current_player == "X":
        return "O"
    else:
        return "X"
