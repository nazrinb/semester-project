from tkinter import simpledialog, messagebox
import tkinter as tk
import pickle
import os

events = {}

# save to memory
def save_events():
    with open("events.pkl", "wb") as file:
        pickle.dump(events, file)

def load_events():
    global events
    if os.path.exists("events.pkl"):
        with open("events.pkl", "rb") as file:
            events = pickle.load(file)

load_events()

# add event function 
def add_event():
    def confirm_event():
        event_name = entry.get().strip()
        if not event_name:
            messagebox.showerror("Error", "Event name cannot be empty.")
            return

        event_date = simpledialog.askstring("Add Event", "Enter event date (YYYY-MM-DD):")
        if event_date:
            events[event_date] = event_name
            save_events()  

            messagebox.showinfo("Success", f"Event '{event_name}' added on {event_date}!")
            event_window.destroy()
            show_year_calendar()  

    # pop-up windows
    event_window = tk.Toplevel(root)
    event_window.title("Add Event")
    event_window.geometry("300x150")  
    event_window.resizable(False, False)  
    event_window.configure(bg="#faf0ca")

    tk.Label(event_window, text="Enter Event Name:", font=("Helvetica", 12, "bold"), bg="#faf0ca", fg="#0d3b66").pack(pady=10)
    
    entry = tk.Entry(event_window, font=("Helvetica", 12), bg="#ffffff", fg="#0d3b66", width=25)
    entry.pack(pady=5)

    button_frame = tk.Frame(event_window, bg="#faf0ca")
    button_frame.pack(pady=10)

    add_button = tk.Button(button_frame, text="Add", font=("Helvetica", 12, "bold"), bg="#faf0ca", fg="#0d3b66", command=confirm_event)
    cancel_button = tk.Button(button_frame, text="Cancel", font=("Helvetica", 12, "bold"), bg="#faf0ca", fg="#0d3b66", command=event_window.destroy)

    add_button.pack(side="left", padx=5)
    cancel_button.pack(side="left", padx=5)
 

def remove_event():
    event_date = simpledialog.askstring("Remove Event", "Enter event date (YYYY-MM-DD):")
    if event_date in events:
        removed_event = events.pop(event_date)
        save_events()  
        messagebox.showinfo("Success", f"Event '{removed_event}' removed from {event_date}!")
        show_year_calendar()  
    else:
        messagebox.showerror("Error", "No event found on that date.")


def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    return 0

def get_start_day(month, year):
    total_days = 0
    for y in range(1900, year):
        total_days += 366 if is_leap_year(y) else 365
    for m in range(1, month):
        total_days += get_days_in_month(m, year)
    return (total_days + 1) % 7

def show_year_calendar():
    for widget in calendar_frame.winfo_children():
        widget.destroy()

    try:
        year = int(year_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid year.")
        return

    year_title.config(text=f"Year {year}")  

    try:
        year = int(year_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid year.")
        return

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    for i, month_name in enumerate(months):
        frame = tk.Frame(calendar_frame, relief="ridge", borderwidth=2, bg="#faf0ca", width=100, height=10)
        frame.pack_propagate(False)  
        frame.grid(row=i // 4, column=i % 4, padx=5, pady=5, sticky="nsew")

        label = tk.Label(frame, text=month_name, font=("Helvetica", 14, "bold"), bg="#faf0ca", fg="#0d3b66")
        label.pack(pady=3)

        days_frame = tk.Frame(frame, bg="#faf0ca")
        days_frame.pack()

        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for day in days:
            tk.Label(days_frame, text=day, width=3, height=1, font=("Helvetica", 8, "bold"), relief="groove", bg="#f4d35e", fg="#0d3b66").grid(row=0, column=days.index(day), padx=1, pady=1)

        days_in_month = get_days_in_month(i + 1, year)
        start_day = get_start_day(i + 1, year)

        row = 1
        col = start_day

        for day in range(1, days_in_month + 1):
            date = f"{year}-{i + 1:02d}-{day:02d}"
            bg_color = "#faf0ca"  
            border_color = "#3d5a80" if date in events else "#faf0ca"  
            

            day_button = tk.Button(
                days_frame, text=str(day), width=3, height=1,
                font=("Helvetica", 8), relief="ridge", bg=bg_color if date in events else "#faf0ca", fg="#0d3b66", 
                highlightbackground=border_color,  
                highlightcolor=border_color,
                highlightthickness=2 if date in events else 0,  
                command=lambda d=date: show_event(d)
            )
            day_button.grid(row=row, column=col, padx=1, pady=1)

            col += 1
            if col > 6:
                col = 0
                row += 1

    calendar_frame.grid_columnconfigure(tuple(range(4)), weight=1)
    calendar_frame.grid_rowconfigure(tuple(range(3)), weight=1)

def show_event(date):
    if date in events:
        messagebox.showinfo("Event", f"Event on {date}: {events[date]}")
    else:
        messagebox.showinfo("No Event", f"No event on {date}.")

root = tk.Tk()
root.title("Yearly Calendar")
root.attributes('-fullscreen', True)
root.configure(bg="#0d3b66")

# Year Entry
top_frame = tk.Frame(root, bg="#0d3b66")
top_frame.pack(fill="x", pady=10)

year_label = tk.Label(top_frame, text="Enter Year:", font=("Helvetica", 16), bg="#0d3b66", fg="#faf0ca")
year_label.pack(side="left", padx=20)

year_entry = tk.Entry(top_frame, font=("Helvetica", 16), bg="#faf0ca", fg="#0d3b66", width=10)
year_entry.pack(side="left", padx=10)

show_button = tk.Button(top_frame, text="Show Calendar", font=("Helvetica", 14), bg="#f4d35e", fg="#0d3b66", command=show_year_calendar)
show_button.pack(side="left", padx=10)

year_title = tk.Label(root, text=f"Year {year_entry.get()}", font=("Helvetica", 32, "italic"), bg="#0d3b66", fg="#faf0ca")
year_title.pack(pady=10)


calendar_frame = tk.Frame(root, bg="#0d3b66")
calendar_frame.pack(expand=True, fill="both", padx=20, pady=10)

button_frame = tk.Frame(root, bg="#0d3b66")
button_frame.pack(side="bottom", pady=20)
button_style = {"font": ("Helvetica", 14, "bold"), "bg": "#faf0ca", "fg": "#0d3b66", "width": 15, "height": 2, "bd": 2, "relief": "ridge"}

add_button = tk.Button(button_frame, text="Add Event", command=add_event, **button_style)
remove_button = tk.Button(button_frame, text="Remove Event", command=remove_event, **button_style)
exit_button = tk.Button(button_frame, text="Exit", command=root.quit, **button_style)

add_button.pack(side="left", padx=10)
remove_button.pack(side="left", padx=10)
exit_button.pack(side="left", padx=10)

root.mainloop()
