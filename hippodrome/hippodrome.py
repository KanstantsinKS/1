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


def view_weather():
    """

    Метод выводит информацию о текущей погоде в информационный чат.
    """
    message = "Сейчас на ипподроме "
    if day_time == 1:
        message += "ночь, "
    elif day_time == 2:
        message += "утро, "
    elif day_time == 3:
        message += "день, "
    elif day_time == 4:
        message += "вечер, "

    if weather == 1:
        message += "льет сильный дождь."
    elif weather == 2:
        message += "бушует ураган."
    elif weather == 3:
        message += "моросит дождик."
    elif weather == 4:
        message += "пасмурно."
    elif weather == 5:
        message += "погода ясная."

    insert_text(message)


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
    if randint(0, 100) < 20:
        problem_horse()

    global x01, x02, x03, x04

    speed01 = (randint(1, day_time + weather) + randint(1, int((7 - state01)) * 3)) / randint(10, 175)
    speed02 = (randint(1, day_time + weather) + randint(1, int((7 - state02)) * 3)) / randint(10, 175)
    speed03 = (randint(1, day_time + weather) + randint(1, int((7 - state03)) * 3)) / randint(10, 175)
    speed04 = (randint(1, day_time + weather) + randint(1, int((7 - state04)) * 3)) / randint(10, 175)

    accelerate = 2

    if accelerate01:
        speed01 *= randint(1, 2 + state01 * (1 + accelerate01 * accelerate))
    if accelerate02:
        speed02 *= randint(1, 2 + state02 * (1 + accelerate02 * accelerate))
    if accelerate03:
        speed03 *= randint(1, 2 + state03 * (1 + accelerate03 * accelerate))
    if accelerate04:
        speed04 *= randint(1, 2 + state04 * (1 + accelerate04 * accelerate))

    if move01:
        if not reverse01:
            x01 += speed01 * 3
        else:
            x01 -= speed01 * 3
    if move02:
        if not reverse02:
            x02 += speed02 * 3
        else:
            x02 -= speed02 * 3
    if move03:
        if not reverse03:
            x03 += speed03 * 3
        else:
            x03 -= speed03 * 3
    if move04:
        if not reverse04:
            x04 += speed04 * 3
        else:
            x04 -= speed04 * 3

    horse_plase_in_window()

    all_move = move01 or move02 or move03 or move04
    all_x = x01 < 0 and x02 < 0 and x03 < 0 and x04 < 0
    all_reverse = reverse01 and reverse02 and reverse03 and reverse04

    if not all_move or all_x or all_reverse:
        win_round(0)
        return 0

    if x01 < 952 and x02 < 952 and x03 < 952 and x04 < 952:
        root.after(5, move_horse)
    else:
        if x01 >= 952:
            win_round(1)
        elif x02 >= 952:
            win_round(2)
        elif x03 >= 952:
            win_round(3)
        elif x04 >= 952:
            win_round(4)


def win_round(horse):
    """

    Метод вызывается когда хотя бы одна лошадь достигла финиша, или если все лошади сошли с дистанции. Производит
    расчет результатов выигрыша или поражения игрока. Выводит сообщение результата. Записывает сумму средств в файл.
    """
    global x01, x02, x03, x04, money
    result = "К финишу пришла лошадь "

    if horse == 1:
        result += name_horse01
        win = count01.get() * win_coeff01
    elif horse == 2:
        result += name_horse02
        win = count02.get() * win_coeff02
    elif horse == 3:
        result += name_horse03
        win = count03.get() * win_coeff03
    elif horse == 4:
        result += name_horse04
        win = count04.get() * win_coeff04

    if horse > 0:
        result += f"! Вы выиграли {int(win)} {currency}. "
        if win > 0:
            result += "Поздравляем! Средства уже зачислены на Ваш счет!"
            insert_text(f"Этот забег принес Вам {int(win)} {currency}.")
        else:
            result += "К сожалению, Ваша лошадь проиграла. Попробуйте снова!"
            insert_text("Делайте ставку!")
        messagebox.showinfo("Результат", result)
    else:
        messagebox.showinfo("Сожалеем!", "Все лошади сошли с дистанции.")
        insert_text("Забег признан несостоявшимся.")
        win = count01.get() + count02.get() + count03.get() + count04.get()

    money += win
    save_money(int(money))

    setup_horse()

    start_button["state"] = "normal"
    bet01["state"] = "readonly"
    bet02["state"] = "readonly"
    bet03["state"] = "readonly"
    bet04["state"] = "readonly"
    bet01.current(0)
    bet02.current(0)
    bet03.current(0)
    bet04.current(0)

    x01, x02, x03, x04 = 20, 20, 20, 20
    horse_plase_in_window()

    refresh_combo(event_objects="")
    view_weather()
    health_horse()
    insert_text(f"Ваши средства {int(money)} {currency}.")

    if money < 1:
        messagebox.showinfo("Стоп!", "На ипподром без денег нельзя!")
        quit(0)


def problem_horse():
    """

    Метот генерации внештатных ситуаций(лошадь развернулась, скидывает жокея, ускоряется).
    """
    global reverse01, reverse02, reverse03, reverse04
    global move01, move02, move03, move04
    global accelerate01, accelerate02, accelerate03, accelerate04

    horse = randint(1, 4)

    max_rand = 10000

    if horse == 1 and move01 == True and x01 > 0:
        if randint(0, max_rand) < state01 * 5:
            reverse01 = True
            messagebox.showinfo("Упс!", f"Лошадь {name_horse01} побежала в другую сторону!")
        elif randint(0, max_rand) < state01 * 5:
            move01 = False
            messagebox.showinfo("Упс!", f"Лошадь {name_horse01} сбросила жокея и остановилась!")
        elif randint(0, max_rand) < state01 * 5 and not accelerate01:
            move01 = True
            messagebox.showinfo("Вау!", f"Лошадь {name_horse01} перестала притворяться и ускорилась!")
    elif horse == 2 and move02 == True and x02 > 0:
        if randint(0, max_rand) < state02 * 5:
            reverse02 = True
            messagebox.showinfo("Упс!", f"Лошадь {name_horse02} побежала в другую сторону!")
        elif randint(0, max_rand) < state02 * 5:
            move02 = False
            messagebox.showinfo("Упс!", f"Лошадь {name_horse02} сбросила жокея и остановилась!")
        elif randint(0, max_rand) < state02 * 5 and not accelerate02:
            accelerate02 = True
            messagebox.showinfo("Вау!", f"Лошадь {name_horse01} перестала притворяться и ускорилась!")
    elif horse == 3 and move03 == True and x03 > 0:
        if randint(0, max_rand) < state03 * 5:
            reverse03 = True
            messagebox.showinfo("Упс!", f"Лошадь {name_horse03} побежала в другую сторону!")
        elif randint(0, max_rand) < state03 * 5:
            move03 = False
            messagebox.showinfo("Упс!", f"Лошадь {name_horse03} сбросила жокея и остановилась!")
        elif randint(0, max_rand) < state03 * 5 and not accelerate03:
            accelerate03 = True
            messagebox.showinfo("Вау!", f"Лошадь {name_horse03} перестала притворяться и ускорилась!")
    elif horse == 4 and move04 == True and x04 > 0:
        if randint(0, max_rand) < state04 * 5:
            reverse04 = True
            messagebox.showinfo("Упс!", f"Лошадь {name_horse04} побежала в другую сторону!")
        elif randint(0, max_rand) < state04 * 5:
            move04 = False
            messagebox.showinfo("Упс!", f"Лошадь {name_horse04} сбросила жокея и остановилась!")
        elif randint(0, max_rand) < state04 * 5 and not accelerate04:
            accelerate04 = True
            messagebox.showinfo("Вау!", f"Лошадь {name_horse04} перестала притворяться и ускорилась!")


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
    global state01, state02, state03, state04
    global weather, day_time
    global win_coeff01, win_coeff02, win_coeff03, win_coeff04
    global move01, move02, move03, move04
    global reverse01, reverse02, reverse03, reverse04
    global accelerate01, accelerate02, accelerate03, accelerate04

    weather = randint(1, 5)
    day_time = randint(1, 4)

    state01 = randint(1, 5)
    state02 = randint(1, 5)
    state03 = randint(1, 5)
    state04 = randint(1, 5)

    win_coeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
    win_coeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
    win_coeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100
    win_coeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100

    reverse01, reverse02, reverse03, reverse04 = False, False, False, False

    move01, move02, move03, move04 = True, True, True, True

    accelerate01, accelerate02, accelerate03, accelerate04 = False, False, False, False


def get_health(name, state, win):
    """
    Функция формирует и возвращает текстовую запись состояния каждой отдельной лошади и коэффициент ставки на нее.
    """
    message = f"Лошадь {name} "
    if state == 5:
        message += "мучается несварением желудка."
    elif state == 4:
        message += "плохо спала. Подергивается веко."
    elif state == 3:
        message += "сурова и беспощадна."
    elif state == 2:
        message += "в отличном настроении."
    elif state == 1:
        message += "просто ракета!"

    message += f" ({win}:1)"
    return message


def health_horse():
    """
    Метод выводит текстовую запись состояния каждой отдельной лошади и коэффициент ставки на нее.
    """
    insert_text(get_health(name_horse01, state01, win_coeff01))
    insert_text(get_health(name_horse02, state02, win_coeff02))
    insert_text(get_health(name_horse03, state03, win_coeff03))
    insert_text(get_health(name_horse04, state04, win_coeff04))


# Инициализация tkinter.
root = Tk()

# Определяем размер окна программы константами.
WIDTH = 1024
HEIGHT = 600

# Устанавливаем координаты x для каждой из лошадей.
x01, x02, x03, x04 = 20, 20, 20, 20

# Задаем переменные кличек лошадей.
name_horse01 = "Ананас"
name_horse02 = "Сталкер"
name_horse03 = "Прожорливый"
name_horse04 = "Копытце"

# Переменные отвечающие за движение назад.
reverse01, reverse02, reverse03, reverse04 = False, False, False, False

# Переменные отвечающие за движение вперед или остановку.
move01, move02, move03, move04 = True, True, True, True

# Переменные отвечающие за ускорение.
accelerate01, accelerate02, accelerate03, accelerate04 = False, False, False, False

# Задаем переменные денег.
money = 0
default_money = 10000
currency = "руб"

# Погода 1 - ливень, 2 - ураган, 3 - дождь, 4 - пасмурно, 5 - ясно
weather = randint(1, 5)

# Время суток 1 - ночь, 2 - утро, 3 - день, 4 - вечер
day_time = randint(1, 4)

# Состояние лошадей 1 - отлично, 5 - ужасно.
state01 = randint(1, 5)
state02 = randint(1, 5)
state03 = randint(1, 5)
state04 = randint(1, 5)

win_coeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
win_coeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
win_coeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100
win_coeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100

# Вычисляем координаты для размещения окна по центру.
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2

# Установка заголовка.
root.title("Hyppodrome")

# Запрещаем изменение размеров окна.
root.resizable(False, False)

# Устанавливаем ширину, высоту и позицию.
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

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

hoese02_game = BooleanVar()
hoese02_game.set(0)
hoese02_check = Checkbutton(text=name_horse02, variable=hoese02_game, onvalue=1, offvalue=0)
hoese02_check.place(x=150, y=478)

hoese03_game = BooleanVar()
hoese03_game.set(0)
hoese03_check = Checkbutton(text=name_horse03, variable=hoese03_game, onvalue=1, offvalue=0)
hoese03_check.place(x=150, y=508)

hoese04_game = BooleanVar()
hoese04_game.set(0)
hoese04_check = Checkbutton(text=name_horse04, variable=hoese04_game, onvalue=1, offvalue=0)
hoese04_check.place(x=150, y=538)

hoese01_check["state"] = "disabled"
hoese02_check["state"] = "disabled"
hoese03_check["state"] = "disabled"
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

view_weather()
health_horse()

# Рисуем окно игры.
root.mainloop()


