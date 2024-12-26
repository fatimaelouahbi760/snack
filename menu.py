
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# =================================================================================
snacks = {
    "Pizza": 40.00,
    "Tacos": 49.00,
    "Sandwich": 30.00,
    "Burger": 32.00,
    "Frites": 15.00,
    "Nuggets": 35.00,
    "Soda": 15.00,
    "Limonade": 18.00
}

# ==================================================================================
def calculate_total():
    total = 0
    for snack, entry in snack_vars.items():
        try:
            quantity = int(entry.get())
            if quantity > 0:
                total += snacks[snack] * quantity
        except ValueError:
            pass
    messagebox.showinfo("le prix de votre commande est : ", 
          f"le prix total est: {total:.2f} €")

# ============================================================================================
root = tk.Tk()

root.title("  snack de fatima")
root.geometry("700x600")
root.resizable(False, False)
root.configure(background="#ffcc66")
root.iconbitmap("menu.ico")
# mabrach ykhdam ==============================================================================

background_image = Image.open("imag.jpg")
background_image = background_image.resize((800, 600), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

background_label = tk.Label(root, image=background_photo)
background_label.place(relwidth=1, relheight=1)

# ============================================================================================
title_label = tk.Label(root, text="Bienvenue  au snak de fatima",
                       font=("Arial", 30, "bold"),
bg="#ffcc66", fg="#4d2600")
title_label.pack(pady=20)

# ========================================================================================================
snack_vars = {}
frame = tk.Frame(root, bg="#ffe6b3")
frame.pack(pady=20)

for snack, price in snacks.items():
    item_frame = tk.Frame(frame, bg="#ffe6b3")
    item_frame.pack(pady=5, fill=tk.X)

    label = tk.Label(item_frame, text=f"{snack} - {price:.2f} €", font=("Arial", 14), bg="#ffe6b3", fg="#4d2600")
    label.pack(side=tk.LEFT, padx=20)

    entry = tk.Entry(item_frame, font=("Arial", 14), width=5)
    entry.pack(side=tk.RIGHT, padx=20)

    snack_vars[snack] = entry

# =========================================================================================
tk.Button(
    root, text="Calculer le prix total", command=calculate_total,
    font=("Helvetica", 16, "bold"), bg="#ff8000", fg="white", padx=20, pady=10
).pack(pady=20)

root.mainloop()

