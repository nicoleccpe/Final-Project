import tkinter as tk
from tkinter import ttk
import random

# List of parks and recreation facilities
facilities = ["Park A", "Park B", "Recreation Center C", "Sports Complex D", "Community Center E"]

# List to store reservations
reservations = []

# Function to add a new reservation
def add_reservation():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    facility = facility_combo.get()
    date = date_entry.get()
    contact = contact_entry.get()
    new_reservation = {"first_name": first_name, "last_name": last_name, "facility": facility, "date": date, "contact": contact}
    reservations.append(new_reservation)
    update_reservation_list()
    clear_entries()

# Function to edit a reservation
def edit_reservation():
    selected_items = reservation_table.selection()
    if selected_items:
        selected_item = selected_items[0]
        reservation = reservations[reservation_table.index(selected_item)]
        first_name_entry.delete(0, tk.END)
        last_name_entry.delete(0, tk.END)
        facility_combo.set(reservation["facility"])
        date_entry.delete(0, tk.END)
        contact_entry.delete(0, tk.END)
        first_name_entry.insert(0, reservation["first_name"])
        last_name_entry.insert(0, reservation["last_name"])
        date_entry.insert(0, reservation["date"])
        contact_entry.insert(0, reservation["contact"])

# Function to save edited reservation
def save_reservation():
    selected_items = reservation_table.selection()
    if selected_items:
        selected_item = selected_items[0]
        reservation_index = reservation_table.index(selected_item)
        reservations[reservation_index] = {
            "first_name": first_name_entry.get(),
            "last_name": last_name_entry.get(),
            "facility": facility_combo.get(),
            "date": date_entry.get(),
            "contact": contact_entry.get()
        }
        update_reservation_list()
        clear_entries()

# Function to delete a reservation
def delete_reservation():
    selected_items = reservation_table.selection()
    if selected_items:
        selected_item = selected_items[0]
        reservation_index = reservation_table.index(selected_item)
        reservations.pop(reservation_index)
        update_reservation_list()

# Function to clear entry fields
def clear_entries():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    facility_combo.set("")
    date_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)

# Function to update the reservation list
def update_reservation_list():
    reservation_table.delete(*reservation_table.get_children())
    for reservation in reservations:
        name = f"{reservation['first_name']} {reservation['last_name']}"
        reservation_table.insert("", tk.END, values=(name, reservation['contact'], reservation['facility'], reservation['date']))

# Function to generate random colors
def random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Create the main window
root = tk.Tk()
root.title("Parks and Recreation Facility Reservation System")
root.geometry("1280x720")  # Full laptop size

# Generate random background color
bg_color = random_color()
root.configure(bg=bg_color)

# Create frames
header_frame = tk.Frame(root, bg=bg_color)
input_frame = tk.Frame(root, bg=bg_color)
list_frame = tk.Frame(root, bg=bg_color)
button_frame = tk.Frame(root, bg=bg_color)

# Create header labels
header_label = tk.Label(header_frame, text="Parks and Recreation Facility Reservation System", font=("Arial", 18, "bold"), bg=bg_color, fg="white")
header_label.pack(pady=10)

# Create input labels and entry fields
input_table = tk.Frame(input_frame, bg=bg_color)
input_table.pack(pady=10)

first_name_label = tk.Label(input_table, text="First Name:", font=("Arial", 12), bg=bg_color, fg="white")
first_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
first_name_entry = tk.Entry(input_table, font=("Arial", 12))
first_name_entry.grid(row=0, column=1, padx=10, pady=5)

last_name_label = tk.Label(input_table, text="Last Name:", font=("Arial", 12), bg=bg_color, fg="white")
last_name_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")
last_name_entry = tk.Entry(input_table, font=("Arial", 12))
last_name_entry.grid(row=0, column=3, padx=10, pady=5)

facility_label = tk.Label(input_table, text="Facility:", font=("Arial", 12), bg=bg_color, fg="white")
facility_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
facility_combo = ttk.Combobox(input_table, values=facilities, font=("Arial", 12), state="readonly")
facility_combo.grid(row=1, column=1, padx=10, pady=5)

date_label = tk.Label(input_table, text="Date (YYYY-MM-DD):", font=("Arial", 12), bg=bg_color, fg="white")
date_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")
date_entry = tk.Entry(input_table, font=("Arial", 12))
date_entry.grid(row=1, column=3, padx=10, pady=5)

contact_label = tk.Label(input_table, text="Contact Number:", font=("Arial", 12), bg=bg_color, fg="white")
contact_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
contact_entry = tk.Entry(input_table, font=("Arial", 12))
contact_entry.grid(row=2, column=1, padx=10, pady=5)

# Create reservation table
reservation_table = ttk.Treeview(list_frame, columns=("Name", "Contact", "Facility", "Date"), show="headings")
reservation_table.heading("Name", text="Name")
reservation_table.heading("Contact", text="Contact Number")
reservation_table.heading("Facility", text="Facility")
reservation_table.heading("Date", text="Reservation Date")
reservation_table.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create scrollbars
yscrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL, command=reservation_table.yview)
yscrollbar.pack(side=tk.RIGHT, fill=tk.Y)
reservation_table.configure(yscrollcommand=yscrollbar.set)

xscrollbar = tk.Scrollbar(list_frame, orient=tk.HORIZONTAL, command=reservation_table.xview)
xscrollbar.pack(side=tk.BOTTOM, fill=tk.X)
reservation_table.configure(xscrollcommand=xscrollbar.set)

# Create buttons
button_frame.pack(pady=10)
add_button = tk.Button(button_frame, text="Add", font=("Arial", 12), bg="green", fg="white", command=add_reservation)
add_button.grid(row=0, column=0, padx=10, pady=10)

edit_button = tk.Button(button_frame, text="Edit", font=("Arial", 12), bg="orange", fg="white", command=edit_reservation)
edit_button.grid(row=0, column=1, padx=10, pady=10)

save_button = tk.Button(button_frame, text="Save Changes", font=("Arial", 12), bg="blue", fg="white", command=save_reservation)
save_button.grid(row=0, column=2, padx=10, pady=10)

delete_button = tk.Button(button_frame, text="Delete", font=("Arial", 12), bg="red", fg="white", command=delete_reservation)
delete_button.grid(row=0, column=3, padx=10, pady=10)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12), bg="gray", fg="white", command=clear_entries)
clear_button.grid(row=0, column=4, padx=10, pady=10)

header_frame.pack(fill=tk.X, padx=10, pady=10)
input_frame.pack(padx=10, pady=10)
list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

root.mainloop()