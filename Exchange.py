import requests
import  json
from tkinter import *
from tkinter import messagebox as mb


def exchange():
    code = entry.get()

    if code:
        try:
            response = requests.get("https://open.er-api.com/v6/latest/USD") # запрос к сайту
            response.raise_for_status() # проверяем на ошибки
            data = response.json() # раскладываем в виде обычного python словаря
            if code in data["rates"]:
                exchange_rate = data['rates'][code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate} {code} за один доллар")
            else:
                mb.showerror("Ошибка", f"Валюта {code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка", f"Произошла ошибка: {e}.")
    else:
        mb.showwarning("Внимание", "Введите код калюты")


window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Введите код валюты").pack(padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)

Button(text="Получить курс обмена к долару", command=exchange).pack(padx=10, pady=10)

window.mainloop()


















# result = requests.get('https://open.er-api.com/v6/latest/USD')
# data = json.loads(result.text)
# p = pprint.PrettyPrinter(indent=4)
# p.pprint(data)