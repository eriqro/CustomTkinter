import customtkinter as ctk
import tkinter as tk
from api import sek_rate as exchange_rate

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.title("Currency Conversion")
window.geometry("400x300")

def exchange():
    try:
        amount = float(userinput.get())
        selected_indices = listbox.curselection()
        if not selected_indices:
            output_text.configure(text="Please select a conversion direction")
            return
        direction = listbox.get(selected_indices[0])
        if direction == "Usd->Sek":
            converted = amount * exchange_rate
            output_text.configure(text=f"{amount} USD is {round(converted, 2)} SEK")
        else:
            converted = amount / exchange_rate
            output_text.configure(text=f"{amount} SEK is {round(converted, 2)} USD")
    except ValueError:
        output_text.configure(text="Please enter a valid number")

def on_select(event):
    selected_indices = listbox.curselection()
    if selected_indices:
        selected_text = listbox.get(selected_indices[0])
        if selected_text == "Usd->Sek":
            topText.configure(text="Currency Conversion\n\nUsd → Sek")
        else:
            topText.configure(text="Currency Conversion\n\nSek → Usd")

topText = ctk.CTkLabel(window, text="Currency Conversion\n\nSelect which exchange")
topText.grid(row=0, column=0, padx=30, pady=20)

userinput = ctk.CTkEntry(window, width=150)
userinput.grid(row=1, column=0, pady=10)

exchangebutton = ctk.CTkButton(window, text="Exchange", command=exchange)
exchangebutton.grid(row=2, column=0, pady=10)

output_text = ctk.CTkLabel(window, text="")
output_text.grid(row=3, column=0, pady=10)

listbox = tk.Listbox(window, height=3)
listbox.grid(row=1, column=1, padx=10, pady=10)
listbox.bind('<<ListboxSelect>>', on_select)

items = ["Usd->Sek", "Sek->Usd"]
for item in items:
    listbox.insert(tk.END, item)

window.mainloop()
