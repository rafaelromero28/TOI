# Python GUI
from tkinter import *
from datetime import datetime
from tkinter import messagebox


root = Tk()
root.title('Move My Motor')

root.geometry("500x500")

b1 = 0


def motor():
    if my_entry.get() and my_entry1.get():
        # Determine value for Speed
        a = float(my_entry.get())
        b = float(my_entry1.get())

        a1 = float((a/.5) * 3200 * 10000)
        b1 = float((b/.5) * 3200)

        # Show in message box
        messagebox.showinfo("Your Age", f"Speed: {a1}")
        messagebox.showinfo("Your Age", f"Distance: {b1}")

    else:
        # Show Error Message
        messagebox.showerror("Error", "You forgot to enter your value!")


# Entry for Speed value
my_label = Label(root, text="Please enter speed value in mm/s",
                 font=("Helvetica", 24))
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

# Entry for Range value
my_label1 = Label(root, text="Please enter range value in mm",
                  font=("Helvetica", 24))
my_label1.pack(pady=20)

my_entry1 = Entry(root, font=("Helvetica", 18))
my_entry1.pack(pady=20)

# Submission button
my_button = Button(root, text="Move Motor",
                   font=("Helvetica", 18), command=motor)
my_button.pack(pady=20)

# Position of Motor
my_label2 = Label(root, text=(f"Distance: {b1}"), font=("Helvetica", 24))
my_label2.pack(pady=20)

root.mainloop()
