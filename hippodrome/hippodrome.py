from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint

def insert_text(string):
    """
    string - строка добавляемая в чат.
    Метод добавляет строку string в информационный чат.
    """
    text_diary.insert(INSERT, string + "\n")
    text_diary.see(END)


def horse_plase_in_window():
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
    global money
    start_button["state"] = "disabled"
    bet01["state"] = "disabled"
    bet02["state"] = "disabled"
    bet03["state"] = "disabled"
    bet04["state"] = "disabled"
    money -= count01.get() + count02.get() + count03.get() + count04.get()
    move_horse()


def move_horse():
    """

    Метод отвечает за расчет положения и движение лошадей. Создает нештатные ситуации. Работает в цикле, вызывается
    каждые 5 милисекунд. Главный цикл игры.
    """
    global x01, x02, x03, x04

    speed01 = randint(3, 10) / 10
    speed02 = randint(3, 10) / 10
    speed03 = randint(3, 10) / 10
    speed04 = randint(3, 10) / 10

    x01 += speed01 * randint(1, 7 - state01) / state01
    x02 += speed02 * randint(1, 7 - state02) / state02
    x03 += speed03 * randint(1, 7 - state03) / state03
    x04 += speed04 * randint(1, 7 - state04) / state04

    horse_plase_in_window()

    if x01 < 952 and x02 < 952 and x03 < 952 and x04 < 952:
        root.after(5, move_horse)


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
    # Динамическое изменение средст на счете игрока.
    count = count01.get() + count02.get() + count03.get() + count04.get()
    label_all_money["text"] = f"У вас на счету: {int(money-count)} {currency}."

    # Динамическое изменение сумму ставки для каждой лошади.
    bet01["values"] = get_values(int(money - count02.get() - count03.get() - count04.get()))
    bet02["values"] = get_values(int(money - count01.get() - count03.get() - count04.get()))
    bet03["values"] = get_values(int(money - count01.get() - count02.get() - count04.get()))
    bet04["values"] = get_values(int(money - count01.get() - count02.get() - count03.get()))

    # Алгоритм включения/выключения чекбоксов, при выборе в них значения.
    if count01.get() > 0:
        hoese01_game.set(True)
    else:
        hoese01_game.set(False)

    if count02.get() > 0:
        hoese02_game.set(True)
    else:
        hoese02_game.set(False)

    if count03.get() > 0:
        hoese03_game.set(True)
    else:
        hoese03_game.set(False)

    if count04.get() > 0:
        hoese04_game.set(True)
    else:
        hoese04_game.set(False)

    # Включение/выключение кнопки Старт.
    if count > 0:
        start_button["state"] = "normal"
    else:
        start_button["state"] = "disabled"


def get_values(count):
    """
    count - сумма средств игрока.
    value - список, который будет возвращен в выпадающее меню.
    Функция формирует список значений ставок для refresh_combo. Шаг ставки 1/10 от общей суммы средств. Возвращает
    список значений для выпадающего меню.
    """
    value = []
    if count > 9:
        for i in range(0, 11):
            value.append(i * (int(count) // 10))
    else:
        value.append(0)
        if count > 0:
            value.append(count)
    return value


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

# Задаем переменные кличек лошадей.
name_horse01 = "Ананас"
name_horse02 = "Сталкер"
name_horse03 = "Прожорливый"
name_horse04 = "Копытце"

# Задаем переменные денег.
money = 0
default_money = 10000
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
horse_plase_in_window()

# Создаем кнопку старта игры и выводим ее на экран.
start_button = Button(text="СТАРТ", font="arial 20", width=61, background="#37AA37")  # Указываем текст кнопки.
start_button.place(x=20, y=370)  # Отрисовка кнопки.
start_button["state"] = "disabled"
start_button["command"] = run_horse

# Создаем информационное поле игры и выводим его на экран.
text_diary = Text(width=70, height=8, wrap=WORD)
text_diary.place(x=430, y=450)

scroll = Scrollbar(command=text_diary.yview, width=20)
scroll.place(x=990, y=450, height=132)
text_diary["yscrollcommand"] = scroll.set

# Выврлим сумму средств на экран.
money = load_money()

# Проверка, если сумма средств меньше или равно 0, выводим диалоговое окно с сообщением и завершаем программу.
if money <= 0:
    messagebox.showinfo("Стоп!", "На ипподром без денег нельзя!")
    quit(0)

# Размещаем сумму средств игрока.
label_all_money = Label(text=f"Осталось средств {money} {currency}.", font="Arial 12")
label_all_money.place(x=20, y=565)

# Располагаем текстовые метки лошадей.
labal_horse01 = Label(text="Ставка на 1 лошадь.")
labal_horse01.place(x=20, y=450)
labal_horse02 = Label(text="Ставка на 2 лошадь.")
labal_horse02.place(x=20, y=480)
labal_horse03 = Label(text="Ставка на 3 лошадь.")
labal_horse03.place(x=20, y=510)
labal_horse04 = Label(text="Ставка на 4 лошадь.")
labal_horse04.place(x=20, y=540)

# Создаем чекбоксы выбора для каждой лошади.
hoese01_game = BooleanVar()
hoese01_game.set(0)
hoese01_check = Checkbutton(text=name_horse01, variable=hoese01_game, onvalue=1, offvalue=0)
hoese01_check.place(x=150, y=448)
hoese01_check["state"] = "disabled"

hoese02_game = BooleanVar()
hoese02_game.set(0)
hoese02_check = Checkbutton(text=name_horse02, variable=hoese02_game, onvalue=1, offvalue=0)
hoese02_check.place(x=150, y=478)
hoese02_check["state"] = "disabled"

hoese03_game = BooleanVar()
hoese03_game.set(0)
hoese03_check = Checkbutton(text=name_horse03, variable=hoese03_game, onvalue=1, offvalue=0)
hoese03_check.place(x=150, y=508)
hoese03_check["state"] = "disabled"

hoese04_game = BooleanVar()
hoese04_game.set(0)
hoese04_check = Checkbutton(text=name_horse04, variable=hoese04_game, onvalue=1, offvalue=0)
hoese04_check.place(x=150, y=538)
hoese04_check["state"] = "disabled"

# Создаем выпадающий список со ставками.
bet01 = ttk.Combobox(root)
bet02 = ttk.Combobox(root)
bet03 = ttk.Combobox(root)
bet04 = ttk.Combobox(root)

bet01["state"] = "readonly"
bet01.place(x=280, y=450)
bet02["state"] = "readonly"
bet02.place(x=280, y=480)
bet03["state"] = "readonly"
bet03.place(x=280, y=510)
bet04["state"] = "readonly"
bet04.place(x=280, y=540)

# Назначаем переменные для хранения ставок, для каждой отдельной лошади.
count01 = IntVar()
count02 = IntVar()
count03 = IntVar()
count04 = IntVar()

# Передаем значения count в bet.
bet01["textvariable"] = count01
bet02["textvariable"] = count02
bet03["textvariable"] = count03
bet04["textvariable"] = count04

# Задаем мето вызываемый при выборе значения из любого Combobox'а.
bet01.bind("<<ComboboxSelected>>", refresh_combo)
bet02.bind("<<ComboboxSelected>>", refresh_combo)
bet03.bind("<<ComboboxSelected>>", refresh_combo)
bet04.bind("<<ComboboxSelected>>", refresh_combo)

refresh_combo("")

bet01.current(0)
bet02.current(0)
bet03.current(0)
bet04.current(0)


# DELETE
bet01.current(1)
refresh_combo("")

# Состояние лошадей 1 - отлично, 5 - ужасно.
state01 = randint(1, 5)
state02 = randint(1, 5)
state03 = randint(1, 5)
state04 = randint(1, 5)

# Рисуем окно игры.
root.mainloop()


