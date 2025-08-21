import tkinter as tk
from api import sek_rate as exchange_rate
window=tk.Tk()
window.title("Currency Convertion")
window.geometry("500x300")

def exchange():
    try:
        Sekinput = float(userinput.get())
        converted=Sekinput/exchange_rate
        output_text.config(text=f"{Sekinput} Sek is {converted} Usd")
    except ValueError:
        output_text.config(text="Please enter a valid number")

topText=tk.Label(window,text="Currency Convertion\n\nSek -> Usd")
topText.pack(pady=20)
userinput=tk.Entry(window,width=20)
userinput.pack(pady=20)
exchangebutton = tk.Button(window, text="Exchange", command=exchange)
exchangebutton.pack(pady=10)
output_text = tk.Label(window, text="")
output_text.pack(pady=20)


window.mainloop()