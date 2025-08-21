import customtkinter as ctk
import tkinter as tk
from api import user_Select

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

window = ctk.CTk()
window.title("Currency Conversion")
window.geometry("400x300")

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

def exchange():
    try:
        user_amount = float(amount_entry.get())
        currency_code = currency_entry.get().strip().upper()
        currency_rate = user_Select(currency_code)
        converted = user_amount * currency_rate
        output_label.configure(text=f"{user_amount} USD is {round(converted, 2)} {currency_code}")
    except ValueError:
        output_label.configure(text="Please enter a valid number")
    except KeyError:
        output_label.configure(text="Currency not found (e.g., SEK, EUR, GBP)")

title_label = ctk.CTkLabel(window, text="Currency Conversion", font=ctk.CTkFont(size=18, weight="bold"))
title_label.grid(row=0, column=0, columnspan=2, pady=20, sticky="ew")

amount_entry = ctk.CTkEntry(window, width=150, placeholder_text="Amount in USD")
amount_entry.grid(row=1, column=0, pady=10, padx=10, sticky="ew")

currency_entry = ctk.CTkEntry(window, width=150, placeholder_text="Currency code (e.g., SEK)")
currency_entry.grid(row=1, column=1, pady=10, padx=10, sticky="ew")

exchange_button = ctk.CTkButton(window, text="Exchange", command=exchange)
exchange_button.grid(row=2, column=0, columnspan=2, pady=10, padx=20, sticky="ew")

output_label = ctk.CTkLabel(window, text="")
output_label.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

window.mainloop()
