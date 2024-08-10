# импортируем библиотеку для работы с HTTP-запросами
import requests
# импортируем модуль для кодирования и декодирования данных в удобном формате
import json
# импортируем библиотеку для работы с графическими объектами
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_c_label(event):
    # Получаем полное название целевой валюты из словаря и обновляем метку
    code = currency_combobox.get()
    name = currency[code]
    c_label.config(text=name)


def exchange_crypto():
    # Создаем функцию обмена криптовалюты
    name_coin = coin_combobox.get()
    name_currency = currency_combobox.get()
    # проверяем, что поля выбора криптовалюты и целевой валюты не пустые
    if name_coin and name_currency:
        try:
            # Запрашиваем данные с сайта
            response = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={name_currency}")
            response.raise_for_status()
            # Переводим данные в формат json
            coin = response.json()
            # Перебираем словари в списке, пока не получим словарь, содержащий название выбранной криптовалюты
            for name in coin:
                if name['name'] == name_coin:
                    exchange_coin = name["current_price"]
                    # Выводим текстовое сообщение с курсом выбранной криптовалюты
                    # по отношению к выбранной целевой валюте
                    mb.showinfo("Курс обмена", f"Курс: {name_coin}:  {exchange_coin} {name_currency}")
                    break
            else:
                mb.showerror("Ошибка", "Криптовалюта или целевая валюта не найдена")

        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")

    else:
        mb.showwarning("Внимание!", "Выберите название криптовалюты!")


# Список названий криптовалют
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
# Словарь кодов валют и их полных названий
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

# Создание графического интерфейса
window = Tk()
window.title("Курсы обмена криптовалют")
window.geometry("360x250")

Label(text="Выберите название криптовалюты").pack(padx=10, pady=10)

coin_combobox = ttk.Combobox(values=coins)
coin_combobox.pack(padx=10, pady=10)

Label(text="Выберите код целевой валюты").pack(padx=10, pady=10)

currency_combobox = ttk.Combobox(values=list(currency.keys()))
currency_combobox.pack(padx=10, pady=10)
currency_combobox.bind("<<ComboboxSelected>>", update_c_label)

c_label = ttk.Label()
c_label.pack(padx=10, pady=10)

Button(text="Получить курс обмена ", command=exchange_crypto).pack(padx=10, pady=10)
window.mainloop()
