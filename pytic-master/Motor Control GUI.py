#tkinter
from tkinter import *
from tkinter import messagebox

#Pololu Motor Controls
import pytic
from time import sleep

# - Initialization -------------------------------------------
tic = pytic.PyTic()
tc = pytic.pytic_protocol.tic_constant

# Connect to first available Tic Device serial number over USB
serial_nums = tic.list_connected_device_serial_numbers()
tic.connect_to_serial_number(serial_nums[0])

# - Initialization of tkinter screen---------------------------
root = Tk()
root.title('Move My Motor')
root.geometry("500x500")


def motor():
    if my_entry.get() and my_entry1.get():
        # Determine value for Speed
        a = float(my_entry.get())
        b = float(my_entry1.get())

        a1 = int((a/.5) * 3200 * 10000)
        b1 = int((b/.5) * 3200)

        # Load configuration file and apply settings
        tic.settings.load_config('pytic-master\config\config.yml')
        tic.settings.max_speed = (a1)
        tic.settings.apply()
        

        # - Motion Command Sequence ----------------------------------
        # Zero current motor position
        tic.halt_and_set_position(0)

        # Energize Motor
        tic.energize()
        tic.exit_safe_start()

        #Speed Controls
        #tic.set_target_velocity(50000)

        # Move to listed positions
        positions = [b1, 0]
        for p in positions:
            tic.set_target_position(p)
            while tic.variables.current_position != tic.variables.target_position:
                sleep(1)

        # De-energize motor and get error status
        tic.enter_safe_start()
        tic.deenergize()
        #print(tic.variables.error_status)

        # Show in message box
        #messagebox.showinfo("Your Age", f"Speed: {a1}")
        #messagebox.showinfo("Your Age", f"Distance: {b1}")

    else:
        # Show Error Message
        messagebox.showerror("Error", "You forgot to enter your value!")


# Entry for Speed value
my_label = Label(root, text="Please enter speed value in mm/s",
                 font=("Helvetica", 20))
my_label.pack(pady=20)

my_entry = Entry(root, font=("Helvetica", 18))
my_entry.pack(pady=20)

# Entry for Range value
my_label1 = Label(root, text="Please enter range value in mm",
                  font=("Helvetica", 20))
my_label1.pack(pady=20)

my_entry1 = Entry(root, font=("Helvetica", 18))
my_entry1.pack(pady=20)

# Submission button
my_button = Button(root, text="Move Motor",
                   font=("Helvetica", 18), command=motor)
my_button.pack(pady=20)

# Position of Motor
my_label2 = Label(root, text=("Distance is {b1}"), font=("Helvetica", 24))
my_label2.pack(pady=20)

root.mainloop()
