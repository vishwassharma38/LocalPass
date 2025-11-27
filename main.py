from tkinter import *
import os, sys
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- Email Memory ------------------------------- #
EMAIL_FILE = "last_email.txt"

def load_last_email():
    if os.path.exists(EMAIL_FILE):
        with open(EMAIL_FILE, "r") as f:
            return f.read().strip()
    return ""

def save_last_email(email):
    with open(EMAIL_FILE, "w") as f:
        f.write(email)

# ---------------------------- Save Password ------------------------------- #
def save():
    website_entry_data = website_entry.get()
    email_entry_data = email_entry.get()
    password_entry_data = password_entry.get()

    if len(website_entry_data) == 0 or len(password_entry_data) == 0 or len(email_entry_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation",
                                       message=f"These are the details entered:\n\nWebsite: {website_entry_data}\nEmail: {email_entry_data}\nPassword: {password_entry_data}\n\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_entry_data} | {email_entry_data} | {password_entry_data}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

            save_last_email(email_entry_data)
            website_entry.focus()

# ---------------------------- Password Generator ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    letters_sample = [random.choice(letters) for _ in range(nr_letters)]
    symbols_sample = [random.choice(symbols) for _ in range(nr_symbols)]
    numbers_sample = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = letters_sample + symbols_sample + numbers_sample

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("LocalPass - Password Manager")
window.config(padx=60, pady=40, bg="#FFFFFF")

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return relative_path

# Logo
try:
    logo_path = resource_path("img/LocalPassLogo.png")
    logo_img = PhotoImage(file=logo_path)
    canvas = Canvas(width=200, height=200, highlightthickness=0, bg="#FFFFFF")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=0, columnspan=3, pady=(0, 20))
except:
    # Fallback if logo doesn't exist
    title_label = Label(text="🔐 LocalPass", font=("Helvetica", 20, "bold"), bg="#FFFFFF", fg="#1A1A1A")
    title_label.grid(row=0, column=0, columnspan=3, pady=(0, 30))

# Configure grid weights for better centering
window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=0)

# Labels with consistent styling
label_font = ("Helvetica", 11)
entry_font = ("Helvetica", 10)

website_label = Label(text="Website:", font=label_font, bg="#FFFFFF", fg="#1A1A1A")
website_label.grid(row=1, column=0, sticky="e", padx=(0, 15), pady=12)

email_label = Label(text="Email/Username:", font=label_font, bg="#FFFFFF", fg="#1A1A1A")
email_label.grid(row=2, column=0, sticky="e", padx=(0, 15), pady=12)

password_label = Label(text="Password:", font=label_font, bg="#FFFFFF", fg="#1A1A1A")
password_label.grid(row=3, column=0, sticky="e", padx=(0, 15), pady=12)

# Entries with consistent styling
website_entry = Entry(width=40, font=entry_font, relief=SOLID, borderwidth=1, bg="#FFFFFF", fg="#1A1A1A")
website_entry.grid(row=1, column=1, columnspan=2, sticky="ew", pady=12, padx=(0, 5))
website_entry.focus()

email_entry = Entry(width=40, font=entry_font, relief=SOLID, borderwidth=1, bg="#FFFFFF", fg="#1A1A1A")
email_entry.grid(row=2, column=1, columnspan=2, sticky="ew", pady=12, padx=(0, 5))

# Autofill last used email if exists
last_email = load_last_email()
if last_email:
    email_entry.insert(0, last_email)

password_entry = Entry(width=26, font=entry_font, relief=SOLID, borderwidth=1, bg="#FFFFFF", fg="#1A1A1A")
password_entry.grid(row=3, column=1, sticky="ew", pady=12, padx=(0, 10))

# Buttons with modern styling
button_font = ("Helvetica", 9, "bold")

generate_password_button = Button(
    text="Generate", 
    command=generate_password,
    font=button_font,
    bg="#E31E24",
    fg="white",
    relief=FLAT,
    padx=15,
    pady=8,
    cursor="hand2",
    activebackground="#C01A1F",
    activeforeground="white"
)
generate_password_button.grid(row=3, column=2, sticky="ew", pady=12, padx=(0, 5))

add_button = Button(
    text="Add Password", 
    command=save,
    font=("Helvetica", 10, "bold"),
    bg="#1A1A1A",
    fg="white",
    relief=FLAT,
    padx=20,
    pady=10,
    cursor="hand2",
    activebackground="#333333",
    activeforeground="white"
)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew", pady=(20, 0), padx=(0, 5))

window.mainloop()