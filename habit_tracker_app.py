import tkinter as tk
from tkinter import messagebox

habits = {}

# Add habit
def add_habit():
    habit = entry.get()
    if habit:
        if habit not in habits:
            habits[habit] = {"done": 0, "total": 0, "streak": 0}
            messagebox.showinfo("Success", "Habit Added!")
            entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Habit already exists!")
    else:
        messagebox.showerror("Error", "Enter a habit name!")

# Mark habit
def mark_done():
    habit = entry.get()
    if habit in habits:
        habits[habit]["done"] += 1
        habits[habit]["total"] += 1
        habits[habit]["streak"] += 1
        messagebox.showinfo("Updated", "Marked as Done!")
    else:
        messagebox.showerror("Error", "Habit not found!")

def mark_not_done():
    habit = entry.get()
    if habit in habits:
        habits[habit]["total"] += 1
        habits[habit]["streak"] = 0
        messagebox.showinfo("Updated", "Marked as Not Done!")
    else:
        messagebox.showerror("Error", "Habit not found!")

# Show progress
def show_progress():
    result = ""
    for h, data in habits.items():
        total = data["total"]
        done = data["done"]
        streak = data["streak"]
        percent = (done / total * 100) if total > 0 else 0

        result += f"{h}\nProgress: {percent:.1f}%\nStreak: {streak} days\n\n"

    if result == "":
        result = "No habits added yet!"

    messagebox.showinfo("Progress", result)

# GUI Window
root = tk.Tk()
root.title("Habit Tracker App")
root.geometry("350x300")

# Title
title = tk.Label(root, text="Habit Tracker", font=("Arial", 16))
title.pack(pady=10)

# Entry
entry = tk.Entry(root, width=25)
entry.pack(pady=5)

# Buttons
btn_add = tk.Button(root, text="Add Habit", command=add_habit)
btn_add.pack(pady=5)

btn_done = tk.Button(root, text="Mark Done", command=mark_done)
btn_done.pack(pady=5)

btn_not_done = tk.Button(root, text="Mark Not Done", command=mark_not_done)
btn_not_done.pack(pady=5)

btn_show = tk.Button(root, text="Show Progress", command=show_progress)
btn_show.pack(pady=10)

# Run app
root.mainloop()
