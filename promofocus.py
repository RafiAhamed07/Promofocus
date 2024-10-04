import tkinter as tk
from tkinter import simpledialog, messagebox
from playsound import playsound
import os
import sys

class FocusTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Focus Timer")
        self.root.geometry("250x100")
        self.root.configure(bg="black")

        # Default settings
        self.work_time = 25  # in minutes
        self.rest_time = 5   # in minutes
        self.cycles = 4

        self.current_cycle = 0
        self.time_left = 0
        self.is_running = False
        self.reset_clicked = False  # Track if reset was clicked

        # Determine the base path for the notification sound
        if hasattr(sys, '_MEIPASS'):
            self.base_path = sys._MEIPASS  # Running as an EXE
        else:
            self.base_path = os.path.abspath(".")

        # Path to the notification sound
        self.notification_sound = os.path.join(self.base_path, 'notifi.mp3')

        # Timer label with increased font size
        self.timer_label = tk.Label(root, text="00:00", font=("Helvetica", 28), bg="black", fg="green")
        self.timer_label.pack(pady=5)

        # Buttons frame
        buttons_frame = tk.Frame(root, bg="black")
        buttons_frame.pack()

        # Start button
        self.start_button = tk.Button(buttons_frame, text="Start", command=self.start_timer, bg="black", fg="green")
        self.start_button.pack(side=tk.LEFT, padx=5)

        # Reset button
        self.reset_button = tk.Button(buttons_frame, text="Reset", command=self.reset_timer, bg="black", fg="green")
        self.reset_button.pack(side=tk.LEFT, padx=5)

        # Settings button
        self.settings_button = tk.Button(buttons_frame, text="Settings", command=self.open_settings, bg="black", fg="green")
        self.settings_button.pack(side=tk.LEFT, padx=5)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.reset_clicked = False  # Reset the flag when starting the timer
            if self.time_left == 0:
                self.time_left = self.work_time * 60  # convert minutes to seconds
            self.update_timer()

    def reset_timer(self):
        self.is_running = False
        self.time_left = 0
        self.current_cycle = 0
        self.timer_label.config(text="00:00")
        self.reset_clicked = True  # Set the flag to true after resetting

    def open_settings(self):
        self.work_time = simpledialog.askinteger("Settings", "Enter work time (minutes):", initialvalue=self.work_time)
        self.rest_time = simpledialog.askinteger("Settings", "Enter rest time (minutes):", initialvalue=self.rest_time)
        self.cycles = simpledialog.askinteger("Settings", "Enter number of cycles:", initialvalue=self.cycles)
        self.reset_timer()

    def play_notification_sound(self):
        playsound(self.notification_sound)  # Play the notification sound

    def update_timer(self):
        if self.is_running and self.time_left > 0:
            mins, secs = divmod(self.time_left, 60)
            time_format = f"{mins:02d}:{secs:02d}"
            self.timer_label.config(text=time_format)
            self.time_left -= 1
            self.root.after(1000, self.update_timer)
        elif self.time_left == 0:
            if self.reset_clicked:
                return  # Do not show any pop-up if reset was clicked

            if self.current_cycle % 2 == 0:
                self.play_notification_sound()
                self.root.lift()  # Bring the window to the front
                messagebox.showinfo("Break Time", "Time for a break!")
            else:
                self.play_notification_sound()
                self.root.lift()  # Bring the window to the front
                messagebox.showinfo("Back to Work", "Break over, back to work!")

            self.current_cycle += 1
            if self.current_cycle < self.cycles * 2:
                self.time_left = self.rest_time * 60 if self.current_cycle % 2 == 1 else self.work_time * 60
                self.update_timer()
            else:
                self.is_running = False
                self.timer_label.config(text="Done!")
                self.play_notification_sound()
                self.root.lift()  # Bring the window to the front
                messagebox.showinfo("Timer Finished", "The focus timer has completed all cycles!")

if __name__ == "__main__":
    root = tk.Tk()
    timer = FocusTimer(root)
    root.mainloop()
