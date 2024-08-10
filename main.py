import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def exchange_crypto():
    name_coin = combobox.get()

#    mb.showinfo("Проверка", name_coin)
    if name_coin:
        try:
            response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd")
            response.raise_for_status()
            coin = response.json()
            for name in coin:
                if name['name'] == name_coin:
                    exchange_coin = name["current_price"]
                    mb.showinfo("Курс обмена", f"Курс: {name_coin}:  {exchange_coin} USD")
                    break
            else:
                mb.showerror("Ошибка", "Криптовалюта не найдена")

        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")

    else:
        mb.showwarning("Внимание!", "Выберите название криптовалюты!")


window = Tk()
window.title("Курсы обмена криптовалют")
window.geometry("360x180")

Label(text="Выберите название криптовалюты").pack(padx=10, pady=10)

coins = [
    "Bitcoin",
    "Ethereum",
    "Tether",
    "BNB",
    "Solana",
    "USDC",
    "XRP",
    "Lido Staked Ether",
    "Toncoin",
    "Dogecoin",
    "Cardano",
    "TRON"
]
combobox = ttk.Combobox(values=coins)
combobox.pack(padx=10, pady=10)


Button(text="Получить курс обмена к доллару", command=exchange_crypto).pack(padx=10, pady=10)
window.mainloop()
