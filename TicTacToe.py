import tkinter as tk
from tkinter import messagebox

turn = "X"
def get_label_text(f, e):
    global turn
    if e.cget("text") == "":
        e.configure(text=turn)
        if block_1.cget("text") != "" and block_1.cget("text") == block_2.cget("text") and block_2.cget("text") == block_3.cget("text"):
            messagebox.showinfo("Message Box", turn+" Win")
        elif block_4.cget("text") != "" and block_4.cget("text") == block_5.cget("text") and block_5.cget("text") == block_6.cget("text"):
            messagebox.showinfo("Message Box", turn+" Win")
        elif block_7.cget("text") != "" and block_7.cget("text") == block_8.cget("text") and block_8.cget("text") == block_9.cget("text"):
            messagebox.showinfo("Message Box", turn+" Win")
        elif block_1.cget("text") != "" and block_1.cget("text") == block_4.cget("text") and block_4.cget("text") == block_7.cget("text"):
            messagebox.showinfo("Message Box", turn+" Win")
        elif block_2.cget("text") != "" and block_2.cget("text") == block_5.cget("text") and block_5.cget("text") == block_8.cget("text"):
            messagebox.showinfo("Message Box", turn+" Win")
        elif block_3.cget("text") != "" and block_3.cget("text") == block_6.cget("text") and block_6.cget("text") == block_9.cget("text"):
            messagebox.showinfo("Message Box", turn+" Win")
        elif block_1.cget("text") != "" and block_1.cget("text") == block_5.cget("text") and block_5.cget("text") == block_9.cget("text"):
            messagebox.showinfo("Message Box", turn+" Win")
        elif block_3.cget("text") != "" and block_3.cget("text") == block_5.cget("text") and block_5.cget("text") == block_9.cget("text"):
            messagebox.showinfo("Message Box", turn+" Win")
        else:
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            label.configure(text="Turn for " + turn)


play_board = tk.Tk()
play_board.geometry("545x370")
play_board.resizable(0, 0)
play_board.configure(bg="grey")

label = tk.Label(play_board, text="Turn for " + turn,
                 width=27, height=2, bg="green", fg="white")
label.grid(row=0, column=0, columnspan=3, pady=(0, 10))
label.configure(font=("verdana", 22, "bold"))

block_1 = tk.Label(play_board, text="", width=7,
                   height=2, bg="black", fg="white")
block_1.grid(row=2, column=0, pady=(0, 1))
block_1.configure(font=("verdana", 27, "bold"))
block_1.bind("<Button-1>", lambda event: get_label_text(1, block_1))

block_2 = tk.Label(play_board, text="", width=7,
                   height=2, bg="black", fg="white")
block_2.grid(row=2, column=1, pady=(0, 1))
block_2.configure(font=("verdana", 27, "bold"))
block_2.bind("<Button-1>", lambda event: get_label_text(2, block_2))

block_3 = tk.Label(play_board, text="", width=7,
                   height=2, bg="black", fg="white")
block_3.grid(row=2, column=2, pady=(0, 1))
block_3.configure(font=("verdana", 27, "bold"))
block_3.bind("<Button-1>", lambda event: get_label_text(3, block_3))

block_4 = tk.Label(play_board, text="", width=7,
                   height=2, bg="black", fg="white")
block_4.grid(row=3, column=0, pady=(0, 1))
block_4.configure(font=("verdana", 27, "bold"))
block_4.bind("<Button-1>", lambda event: get_label_text(4, block_4))

block_5 = tk.Label(play_board, text="", width=7,
                   height=2, bg="black", fg="white")
block_5.grid(row=3, column=1, pady=(0, 1))
block_5.configure(font=("verdana", 27, "bold"))
block_5.bind("<Button-1>", lambda event: get_label_text(5, block_5))

block_6 = tk.Label(play_board, text="", width=7,
                   height=2, bg="black", fg="white")
block_6.grid(row=3, column=2, pady=(0, 1))
block_6.configure(font=("verdana", 27, "bold"))
block_6.bind("<Button-1>", lambda event: get_label_text(6, block_6))

block_7 = tk.Label(play_board, text="", width=7,
                   height=2, bg="black", fg="white")
block_7.grid(row=4, column=0)
block_7.configure(font=("verdana", 27, "bold"))
block_7.bind("<Button-1>", lambda event: get_label_text(7, block_7))

block_8 = tk.Label(play_board, text="", width=7,
                   height=2, bg="black", fg="white")
block_8.grid(row=4, column=1)
block_8.configure(font=("verdana", 27, "bold"))
block_8.bind("<Button-1>", lambda event: get_label_text(8, block_8))

block_9 = tk.Label(play_board, text="", width=7,
                   height=2, bg="black", fg="white")
block_9.grid(row=4, column=2)
block_9.configure(font=("verdana", 27, "bold"))
block_9.bind("<Button-1>", lambda event: get_label_text(9, block_9))

play_board.mainloop()
