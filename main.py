import tkinter as tk

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

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

    year = int(year_entry.get())

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    for i, month_name in enumerate(months):
        frame = tk.Frame(calendar_frame, relief="ridge", borderwidth=2, bg="#faf0ca")
        frame.grid(row=i // 4, column=i % 4, padx=10, pady=10, sticky="nsew")

        label = tk.Label(frame, text=month_name, font=("Helvetica", 14, "bold"), bg="#faf0ca", fg="#0d3b66")
        label.pack(pady=5)

        days_frame = tk.Frame(frame, bg="#faf0ca")
        days_frame.pack(pady=5)

        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for day in days:
            tk.Label(days_frame, text=day, width=5, height=2, anchor="center", font=("Helvetica", 10, "bold"), relief="groove", bg="#f4d35e", fg="#0d3b66").grid(row=0, column=days.index(day), padx=2, pady=2)

        days_in_month = get_days_in_month(i + 1, year)
        start_day = get_start_day(i + 1, year)

        row = 1
        col = start_day

        for day in range(1, days_in_month + 1):
            tk.Label(days_frame, text=str(day), width=5, height=2, anchor="center", font=("Helvetica", 10), relief="ridge", bg="#faf0ca", fg="#0d3b66").grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 6:
                col = 0
                row += 1

root = tk.Tk()
root.title("Yearly Calendar")

root.attributes('-fullscreen', True)
root.configure(bg="#0d3b66")

year_label = tk.Label(root, text="Enter Year:", font=("Helvetica", 16), bg="#0d3b66", fg="#faf0ca")
year_label.pack(pady=20)

year_entry = tk.Entry(root, font=("Helvetica", 16), bg="#faf0ca", fg="#0d3b66")
year_entry.pack(pady=20)

show_button = tk.Button(root, text="Show Year Calendar", font=("Helvetica", 16), bg="#f4d35e", fg="#0d3b66", command=show_year_calendar)
show_button.pack(pady=20)

calendar_frame = tk.Frame(root, bg="#0d3b66")
calendar_frame.pack(expand=True, fill="both", padx=20, pady=20)

root.mainloop()
