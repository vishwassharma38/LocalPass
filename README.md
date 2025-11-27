# LocalPass — Lightweight Local Password Manager

LocalPass is a simple desktop password manager designed for users who prefer full control over their data.  
It stores all saved credentials **locally on your machine**, in a plain-text `.txt` file, ensuring the easiest possible accessibility without relying on external databases, cloud syncing, or account creation.

LocalPass focuses on minimalism, transparency, and offline convenience.

---

## Features

### 🔐 Local Storage
All passwords are stored in a `data.txt` file inside the app directory.  
This gives you complete ownership of your data and full offline functionality.

### ✉️ Email Autofill Memory
The app remembers the **last used email address** and autofills it on the next launch.  
This is saved in `last_email.txt`.

### ⚙️ Built-in Password Generator
LocalPass includes a simple random password generator that creates secure passwords using:
- Uppercase letters  
- Lowercase letters  
- Numbers  
- Symbols  

Generated passwords are automatically copied to your clipboard.

### 🪟 Clean Tkinter UI
The interface uses a neat and minimal design, featuring:
- A logo (if available)  
- Centered layout  
- Modern-styled buttons  
- Plain and accessible text fields  

### 📝 Plaintext Data Format
Saved entries follow this structure:
Website | Email/Username | Password


This plaintext format is intentionally simple for users who want direct access without encryption layers.

---

## How It Works

### Saving Passwords
When you enter a website, email, and password:
1. The app validates that none of the fields are empty.  
2. It asks you for confirmation.  
3. It appends the entry to `data.txt`.  
4. It remembers the entered email for next time.

### Generating Passwords
The "Generate" button:
- Creates a mixed-character password
- Inserts it directly into the password field
- Automatically copies it to your clipboard

### Email Memory System
- On startup, the app reads from `last_email.txt`
- If a saved email exists, it autofills it
- Every time you save a new password, the email is updated

---

## Installation & Usage

1. Make sure you have **Python 3.x** installed.
2. Install dependencies:
   ```bash
   pip install pyperclip

LocalPass/
│
├── main.py               # The main application script
├── data.txt              # Stored passwords (auto-created)
├── last_email.txt        # Email memory file (auto-created)
└── img/
    └── LocalPassLogo.png # Optional logo file

**Notes**

LocalPass does not use encryption.
This is intentional for simplicity and file accessibility, but it means you must protect data.txt yourself.

The project is ideal for local, personal, offline use.

License

This project is free to use, modify, and distribute as you like.
Add any additional license terms here if needed.


