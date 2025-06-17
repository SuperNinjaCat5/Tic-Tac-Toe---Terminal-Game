import tkinter as tk
import ultils

root = tk.Tk()
root.resizable(False, False)
root.geometry("600x400")
root.title("Tic Tac Toe")

winstate = False
current_player = "X"
label = tk.Label(root, text=f"It's player {current_player}'s turn!")
label.pack()

buttons = []

def setup():
    frame = tk.Frame(root, width=50, height=50)
    frame.pack(pady=25)

    for i in range(3):
        frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(i, weight=1)

    for r in range(3):
        row_buttons = []
        for c in range(3):
            box = tk.Button(frame, text="", command=lambda r=r, c=c: player_clicked(r,c), width=10, height=5)
            box.grid(row=r, column=c)
            row_buttons.append(box)
        buttons.append(row_buttons)

def reset_game():
    global current_player, winstate
    current_player = "X"
    winstate = False
    label.config(text=f"It's player {current_player}'s turn!")
    for row in buttons:
        for button in row:
            button.config(text="", relief="raised", state="normal")

def player_clicked(r, c):
    global current_player, winstate
    if winstate:
        return
    btn = buttons[r][c]
    if btn.cget("text") != "":
        return 
    btn.config(text=current_player, relief="sunken")


    def check_line(cells):
        return all(buttons[x][y].cget("text") == current_player for x, y in cells)

    row_cells = [(r, i) for i in range(3)]
    col_cells = [(i, c) for i in range(3)]
    diag1 = [(i, i) for i in range(3)]
    diag2 = [(i, 2 - i) for i in range(3)]

    if (check_line(row_cells) or check_line(col_cells) or
        (r == c and check_line(diag1)) or
        (r + c == 2 and check_line(diag2))):
        label.config(text=f"{current_player} WINS!!!!")
        winstate = True

        for row in buttons:
            for b in row:
                b.config(state="disabled")
        root.after(3000, reset_game)
        return

    current_player = ultils.toggle_xy(current_player)
    label.config(text=f"It's player {current_player}'s turn!")

setup()
root.mainloop()
