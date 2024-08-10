import requests
import json
from tkinter import *
from tkinter import messagebox as mb

def exchange():
    name_coin = entry.get()
    response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd")
    response.raise_for_status()
    coin = response.json()
    for name in coin:
        if name['id'] == name_coin:
            print(name["id"], name["current_price"])


window = Tk()
window.title("Курсы обмена криптовалют")
window.geometry("360x180")

Label(text="Введите название криптовалюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack()



Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10, pady=10)
window.mainloop()
