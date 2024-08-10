import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(event):
    code = currency_combobox.get()
    name = currency[code]
    c_label.config(text=name)


def exchange_crypto():
    name_coin = coin_combobox.get()
    name_currency = currency_combobox.get()
#    mb.showinfo("Проверка", name_coin)
    if name_coin and name_currency:
        try:
            response = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={name_currency}")
            response.raise_for_status()
            coin = response.json()
            for name in coin:
                if name['name'] == name_coin:
                    exchange_coin = name["current_price"]
                    mb.showinfo("Курс обмена", f"Курс: {name_coin}:  {exchange_coin} {name_currency}")
                    break
            else:
                mb.showerror("Ошибка", "Криптовалюта не найдена")

        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")

    else:
        mb.showwarning("Внимание!", "Выберите название криптовалюты!")


window = Tk()
window.title("Курсы обмена криптовалют")
window.geometry("360x250")

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

currency = {
    'rub': "Российский рубль",
    'eur': "Евро",
    'jpy': "Японская йена",
    'cny': "Китайский юань",
    'krw': "Южнокорейская вона",
    'aed': "Дирхам ОАЭ",
    'cad': "Канадский доллар",
    'usd': "Американский доллар",
    'try': "Турецкая лира",
    'ars': "Аргентинский песо"
}

coin_combobox = ttk.Combobox(values=coins)
coin_combobox.pack(padx=10, pady=10)

currency_combobox = ttk.Combobox(values=list(currency.keys()))
currency_combobox.pack(padx=10, pady=10)
currency_combobox.bind("<<ComboboxSelected>>", update_c_label)

c_label = ttk.Label()
c_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена ", command=exchange_crypto).pack(padx=10, pady=10)
window.mainloop()
