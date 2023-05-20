import tkinter as tk

# Создаем окно
root = tk.Tk()
root.title("Крестики-нолики")
root.configure(bg="#00a3cc")

# Создаем кнопки
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text="", font=("Helvetica", 40), width=6, height=3, bg="#0077b3", fg="white", command=lambda i=i, j=j: on_click(i, j))
        button.grid(row=i, column=j, padx=5, pady=5)
        row.append(button)
    buttons.append(row)

# Игровая логика
current_player = "X"
game_over = False

def on_click(i, j):
    global current_player, game_over
    if not game_over and buttons[i][j]["text"] == "":
        buttons[i][j]["text"] = current_player
        if check_win():
            game_over = True
            label["text"] = f"Победил {current_player}!"
        elif check_tie():
            game_over = True
            label["text"] = "Ничья!"
        else:
            current_player = "O" if current_player == "X" else "X"
            label["text"] = f"Ходит {current_player}"

def check_win():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True
    return False

def check_tie():
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                return False
    return True

# Создаем метку для отображения текущего игрока
label = tk.Label(root, text=f"Ходит {current_player}", font=("Helvetica", 24), bg="#00a3cc", fg="white")
label.grid(row=3, column=0, columnspan=3)

# Запускаем игру
root.mainloop()