import tkinter as tk
from tkinter import messagebox
import json
import os
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)

root = tk.Tk()
root.title("CONTACT BOOK")
root.geometry("600x500")

dark_mode = False

contacts = {}

if os.path.exists("contacts.json"):
    with open("contacts.json", "r") as file:
        contacts = json.load(file)

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


def add_contact():
    name = entry_name.get().strip()
    phone = entry_phone.get().strip()
    email = entry_email.get().strip()
    age = entry_age.get().strip()
    address = entry_address.get().strip()

    if name and phone:
        contacts[name] = {"phone": phone, "email": email, "age": age, "address": address}
        save_contacts()
        engine.say("Contact added successfully!")
        engine.runAndWait()
        messagebox.showinfo("Success", f"Contact {name} added successfully!")
        
    else:
        engine.say("Attention: Please enter Name and Phone!")
        engine.runAndWait()
        messagebox.showwarning("Error", "Name and Phone are required!")

def search_contact():
    name = entry_search.get().strip().lower()  # Convert input to lowercase
    found_contact = None
    
    for contact_name in contacts:
        if contact_name.lower() == name:  # Compare in lowercase
            found_contact = contacts[contact_name]
            break

    if found_contact:
        engine.say("Congrats!")
        engine.runAndWait()
        messagebox.showinfo(
            "Contact Found", 
            f"Name: {contact_name}\nPhone: {found_contact['phone']}\nEmail: {found_contact['email']}\nAge: {found_contact['age']}\nAddress: {found_contact['address']}"
        )
    else:
        engine.say("Contact not found!")
        engine.runAndWait()
        messagebox.showerror("Not Found", "Contact not found!")

def delete_contact():
    name = entry_search.get().strip()
    if name in contacts:
        engine.say("deleted successfully!")
        engine.runAndWait()
        del contacts[name]
        save_contacts()
        messagebox.showinfo("Deleted", f"Contact {name} deleted successfully!")
    else:
        engine.say("Contact not found!")
        engine.runAndWait()
        messagebox.showerror("Error", "Contact not found!")

def count_contacts():
    total = len(contacts)
    engine.say(f"Total Contacts: {total}")
    engine.runAndWait()
    messagebox.showinfo("Total Contacts", f"Total Contacts: {total}")

def view_contacts():
    if contacts:
        engine.say("Attention Please!")
        engine.runAndWait()
        sorted_contacts = sorted(contacts.items())  # Sorting contacts alphabetically
        contact_list = "\n".join([f"{name} : {details['phone']} {details['email']} {details['address']} {details['age'] }" for name, details in sorted_contacts])
        messagebox.showinfo("All Contacts", contact_list)
    else:
        messagebox.showinfo("All Contacts", "No contacts available.")

def toggle_dark_mode():
    global dark_mode
    dark_mode =  not dark_mode
    
    if dark_mode:
        root.config(bg="black")
        for widget in root.winfo_children():
            widget.config(bg="black", fg="white")
        toggle_button.config(text="Light Mode", bg="gray")

    else:
        root.config(bg="white")
        for widget in root.winfo_children():
            widget.config(bg="white", fg="black")
        toggle_button.config(text="Dark Mode", bg="lightgray")

title_label = tk.Label(root, text="Contact Book", font=("Arial", 16, "bold"), fg="red")
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5, padx=10, fill="x")
label = tk.Label(frame, text="Contact Name",  fg="black", width=15, anchor="w")
label.pack(side="left", padx=5)
entry_name = tk.Entry(frame, width=30)
entry_name.pack(side="left", padx=5)

frame = tk.Frame(root)
frame.pack(pady=5, padx=10, fill="x")
label = tk.Label(frame, text="Phone Number",  fg="black", width=15, anchor="w")
label.pack(side="left", padx=5)
entry_phone = tk.Entry(frame, width=30)
entry_phone.pack(side="left", padx=5)

frame = tk.Frame(root)
frame.pack(pady=5, padx=10, fill="x")
label = tk.Label(frame, text="Email",  fg="black", width=15, anchor="w")
label.pack(side="left", padx=5)
entry_email = tk.Entry(frame, width=30)
entry_email.pack(side="left", padx=5)

frame = tk.Frame(root)
frame.pack(pady=5, padx=10, fill="x")
label = tk.Label(frame, text="Age",  fg="black", width=15, anchor="w")
label.pack(side="left", padx=5)
entry_age = tk.Entry(frame, width=30)
entry_age.pack(side="left", padx=5)

frame = tk.Frame(root)
frame.pack(pady=5, padx=10, fill="both")
label = tk.Label(frame, text="Address",  fg="black", width=15, anchor="w")
label.pack(side="left", padx=5)
entry_address = tk.Entry(frame, width=30)
entry_address.pack(side="left", padx=5)


button_frame = tk.Frame(root, bg="#222")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Contact", bg="#555", fg="white", command=add_contact).pack(side="left", padx=5)
tk.Button(button_frame, text="Search Contact", bg="#555", fg="white", command=search_contact).pack(side="left", padx=5)
tk.Button(button_frame, text="Delete", bg="#555", fg="white", command=delete_contact).pack(side="left", padx=5)
tk.Button(button_frame, text="View All", bg="#555", fg="white", command=view_contacts).pack(side="left", padx=5)
tk.Button(button_frame, text="Count Contacts", bg="#555", fg="white", command=count_contacts).pack(side="left", padx=5)

tk.Label(root, text="Search Contact").pack()
entry_search = tk.Entry(root)
entry_search.pack()


toggle_button = tk.Button(root, text="Dark Mode", command=toggle_dark_mode, bg="lightgray")
toggle_button.pack(pady=5)

tk.Button(root, text="Exit", command=root.quit).pack(pady=5)

root.mainloop()