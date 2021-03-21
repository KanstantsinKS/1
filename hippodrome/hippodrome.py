from tkinter import *
from tkinter import messagebox

def insert_text(string):
    """
    string - строка добавляемая в чат.
    Метод добавляет строку string в информационный чат.
    """
    text_diary.insert(INSERT, string + "\n")
    text_diary.see(END)


def hourse_plase_in_window():
    """
    horse01..04 - изображение лошади 01..04. ГЛОБАЛЬНЫЕ переменные
    x01..04 - координата х лошади 01..04.
    Метод рисует иконки лошадей в окне игры.
    """
    horse01.place(x=int(x01), y=20)
    horse02.place(x=int(x02), y=100)
    horse03.place(x=int(x03), y=180)
    horse04.place(x=int(x04), y=260)


def load_money():
    """
    money_in_file - сумма денег игрока полученная из файла
    default_money - количество денег по умолчанию, при невозможности открыть файл
    currency - запись названия игровой валюты.
    Метод загружает сумму средств игрока из файла money.dat.
    """
    try:
        file = open("money.dat", "r")
        money_in_file = int(file.readline())
        file.close()
    except FileNotFoundError:
        print(f" Файла сохранения не существует, задано значение {default_money} {currency}.")
        money_in_file = default_money
    return money_in_file


def save_money(money_to_save):
    """
    money_to_save - количество денег на счету пользователя.
    Метод записывает сумму средств игрока из аргумента money_to_save в файл money.dat.
    """
    try:
        file = open("money.dat", "w")
        file.write(str(money_to_save))
        file.close()
    except:
        print(" Ошибка создания файла, наш ипподром закрывается!")
        quit(0)


def view_money():
    """

    Метод выводит в информационый чат оставшуюся у игрока сумму средств.
    """
    pass


def view_weather():
    """

    Метод выводит информацию о текущей погоде в информационный чат.
    """
    pass


def run_horse():
    """

    Метод запускает забег при нажатии кнопки "Старт". Делает неактивными поля выбора ставки. Запускает move_horse
    """
    pass


def move_horse():
    """

    Метод отвечает за расчет положения и движение лошадей. Создает нештатные ситуации. Работает в цикле, вызывается
    каждые 5 милисекунд. Главный цикл игры.
    """
    pass


def win_round(horse):
    """

    Метод вызывается когда хотя бы одна лошадь достигла финиша, или если все лошади сошли с дистанции. Производит
    расчет результатов выигрыша или поражения игрока. Выводит сообщение результата. Записывает сумму средств в файл.
    """
    pass


def problem_horse():
    """

    Метот генерации внештатных ситуаций(лошадь развернулась, скидывает жокея, ускоряется).
    """
    pass


def refresh_combo(event_objects):
    """

    Метод расчитывает значения ставак на основе средст игрока.
    """
    pass


def get_values(count):
    """

    Функция формирует список значений ставок для refresh_combo. Шаг ставки 1/10 от общей суммы средств. Возвращает
    список значений для выпадающего меню.
    """
    pass


def setup_horse():
    """

    Метод устанавливает состояния лошадей и погоды на основе случайных значений. Задается один раз в начале программы
    и обновляется после каждого забега.
    """
    pass


def get_health(name, state, win):
    """

    Функция формирует и возвращает текстовую запись состояния каждой отдельной лошади и коэффициент ставки на нее.
    """
    pass

# Инициализация tkintera.
root = Tk()


# Определяем размер окна программы константами.
WIDTH = 1024
HEIGHT = 600

# Устанавливаем координаты x для каждой из лошадей.
x01 = 20
x02 = 20
x03 = 20
x04 = 20

# Задаем переменные денег.
money = 0
default_money = 0
currency = "руб."

# Вычисляем координаты для размещения окна по центру.
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Устанавливаем ширину, высоту и позицию.
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

# Запрещаем изменение размеров окна.
root.resizable(False, False)

# Установка заголовка.
root.title("Hyppodrome")

# Выводим на экран фон дорожек ипподрома и финишной линии.
road_image = PhotoImage(file="img/road.png")  # Загружаем изображение.
road = Label(root, image=road_image)          # Передаем его в Label.
road.place(x=0, y=17)                         # Выводим на экран.

# Выводим на экран лошадей.
horse01_image = PhotoImage(file="img/horse01.png")  # Загружаем изображение.
horse01 = Label(root, image=horse01_image)          # Передаем его в Label.

horse02_image = PhotoImage(file="img/horse02.png")  # Загружаем изображение.
horse02 = Label(root, image=horse02_image)          # Передаем его в Label.

horse03_image = PhotoImage(file="img/horse03.png")  # Загружаем изображение.
horse03 = Label(root, image=horse03_image)          # Передаем его в Label.

horse04_image = PhotoImage(file="img/horse04.png")  # Загружаем изображение.
horse04 = Label(root, image=horse04_image)          # Передаем его в Label.

# Отрисовываем лошадей на экране.
hourse_plase_in_window()

# Создаем кнопку старта игры и выводим ее на экран.
start_button = Button(text="СТАРТ", font="arial 20", width=61, background="#37AA37")  # Указываем текст кнопки.
start_button.place(x=20, y=370)  # Отрисовка кнопки.

# Создаем информационное поле игры и выводим его на экран.
text_diary = Text(width=70, height=8, wrap=WORD)
text_diary.place(x=430, y=450)

scroll = Scrollbar(command=text_diary.yview, width=20)
scroll.place(x=990, y=450, height=132)
text_diary["yscrollcommand"] = scroll.set

# Выврлим сумму средств на экран.
money = load_money()

if money <= 0:
    messagebox.showinfo("Стоп!", "На ипподром без денег нельзя!")
    quit(0)

label_all_money = Label(text=f"Осталось средств {money} {currency}.", font="Arial 12")
label_all_money.place(x=20, y=565)


root.mainloop()


