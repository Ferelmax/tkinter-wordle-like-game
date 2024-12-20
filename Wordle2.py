import tkinter as tk
import random
import tkinter.messagebox as messagebox

words = [
"apple", "beach", "chair", "dance", "image",
"frail", "crisp", "blunt", "lemon", "moon",
"night", "smile", "frost", "faith", "elite"
"chain", "slime", "snail", "quick", "quark"
"joker", "codex", "squad", "valve", "biker"
]

tries_left = 0
rand_word = ""
current_row = 0
guess_labels = []

def reset():
  global rand_word, tries_left, current_row, guess_labels

  rand_word = words[random.randint(0,len(words) - 1)]
  
  tries_left = 5
  current_row = 0

  for row in guess_labels:
    for label in row:
      label.config(bg = "#635985", text = " ")
      
  tries_label.config(text = f"Tries left: {tries_left}")

  entry.delete(0, tk.END)


def check_guess(event = None):
  global tries_left, current_row, rand_word
  guess = entry.get().lower()

  if len(guess) != 5:
    messagebox.showwarning("Invalid guess", "Please enter a 5-letter word.")
    return

  result = []
  for i in range(5):
    print(i)
    if guess[i] == rand_word[i]:
      result.append("C")
    elif guess[i] in rand_word:
      result.append("IP")
    else:
      result.append("I")

  for j, status in enumerate(result):
    if status == "C":
      guess_labels[current_row][j].config(bg = "Green", text = guess[j].upper())
    elif status == "IP":
      guess_labels[current_row][j].config(bg = "Yellow", text = guess[j].upper())
    else:
      guess_labels[current_row][j].config(bg = "Gray", text = guess[j].upper())
  
  if result == ["C","C","C","C","C"]:
    messagebox.showinfo("Congratulations!", f"The word was {rand_word}")
    reset()
    return

  tries_left -= 1
  tries_label.config(text = f"Tries left: {tries_left}")

  if tries_left == 0:
    messagebox.showinfo("Game Over", f"You ran out of tries, the word was: {rand_word}")
    reset()
    return

  current_row += 1
  entry.delete(0, tk.END)

    
window = tk.Tk()
window.title("Wordle Game")
window.geometry("400x400")
window.config(bg = "#393053")

title = tk.Label(window, text = "Wordle Game", font = "Roboto 16 bold", fg = "white", bg = "#393053")
title.pack(pady = 5)

tries_label = tk.Label(window, text = "Tries left: 5", font = "Roboto 12", fg = "white", bg = "#393053")
tries_label.pack(pady = 5)

guess_frame = tk.Frame(window)
guess_frame.pack(pady = 5)

prompt_label = tk.Label(window, text = "Type you guess:", font = "Roboto 8", fg = "white", bg = "#393053")
prompt_label.pack()

entry = tk.Entry(window, font = "Roboto 12", width = 10, highlightthickness = 0,bd = 0, bg = "#635985", fg = "White")
entry.insert(0, "Type your guess...")
entry.pack(pady = 10)

entry.bind("<Return>", check_guess)

guess_labels = []
for i in range(5):
  row_frame = tk.Frame(guess_frame, bg = "#393053")
  row_frame.pack()
  row_labels = []
  for j in range(5):
    label = tk.Label(row_frame, text = " ", relief = tk.RAISED, width = 2, font = "Roboto 12", bg = "#635985", bd = 0)
    label.pack(side = tk.LEFT, padx = 2, pady = 2)
    row_labels.append(label)
  guess_labels.append(row_labels)

reset()

tk.mainloop()