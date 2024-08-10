import requests
import json
from tkinter import *
from tkinter import messagebox as mb


def exchange_crypto():
    name_coin = entry.get()
#    mb.showinfo("Проверка", name_coin)
    if name_coin:
        try:
            response = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd")
            response.raise_for_status()
            coin = response.json()
            for name in coin:
                if name['id'] == name_coin:
                    exchange_coin = name["current_price"]
                    mb.showinfo("Курс обмена", f"Курс: {name_coin}:  {exchange_coin} USD")
                else:
                    mb.showerror("Ошибка", "Криптовалюта не найдена")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")

    else:
        mb.showwarning("Внимание!", "Введите название криптовалюты!")





window = Tk()
window.title("Курсы обмена криптовалют")
window.geometry("360x180")

Label(text="Введите название криптовалюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack()


Button(text="Получить курс обмена к доллару", command=exchange_crypto).pack(padx=10, pady=10)
window.mainloop()
