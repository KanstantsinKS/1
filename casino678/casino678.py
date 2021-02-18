import os
import ctypes as ctp


valuta = "Rub"
money = 0
defaultMoney = 10000
ctp.windll.Kernel32.GetStdHandle.restype = ctp.c_ulong
h = ctp.windll.Kernel32.GetStdHandle(ctp.c_ulong(0xFFFFFFF5))


def main():
    """
    Главный метод игры.
    """
    pass


def getInput(digit, message):
    """
    digit - возможные для ввода значения в формате строки 0123.
    message - строка-приглашения при входе.
    ret - введенный пользователем симол.
    Функция ввода значения.
    """
    color(7)
    ret = ""
    while (ret == "" or not ret in digit):
    	ret = input(message)
    return ret

#print(f"Вы ввели число {getInput('12', 'Введите 1 или 2! ')}")


def getIntInput(minimum, maximum, message):
    """
    minimum - нижняя граница диапазона(включительно).
    maximum - верхняя граница диапазона(включительно).
    message - текст строки-приглашения ввода.
    st - переменная, хранящая введенную строку.
    Функция ввода целого числа.
    Данная функция вызывается в местах, где требуется ввод пользователя, выбор пункта меню или ввод строки.
    """
    color(7)
    ret = -1
    while (ret < minimum or ret > maximum):
    	st = input(message)
    	if (st.isdigit()):
    		ret = int(st)
    	else:
    		print("    Введи целое число! ")
    return ret

#a = getIntInput(0, 10, "Введи число от 0 до 10: ")
#print(a)


def loadMoney():
    """
    moneyInFile - сумма денег игрока полученная из файла
    defaultMoney - количество денег по умолчанию, при невозможности открыть файл
    valuta - запись названия игровой валюты.
    Метод загружает сумму средств игрока из файла money.dat.
    """
    try:
    	file = open("money.dat", "r")
    	moneyInFile = int(file.mreadLine())
    	file.close()
    except FileNoTFoundError:
    	print(f"Файла сохранения не существует, задано значение {defaultMoney} {valuta}")
    	moneyInFile = defaultMoney
    return moneyInFile


def saveMoney(moneyToSave):
    """
    moneyToSave - количество денег на счету пользователя.
    Метод записывает сумму средств игрока из аргумента moneyToSave в файл money.dat.
    """
    try:
    	file = open("money.dat", "w")
    	file.write(str(moneyToSave))
    	file.close()
    except:
    	print("Ошибка создания файла, наше казино закрывается!")
    	quit(0)

def color(c):
    """
    с - номер цвета для установки.
    Метод установки цвета текста в консоли.
    """
    ctp.windll.Kernel32.SetConsoleTextAttribute(h, c)

#for i in range(16):
#	color(i)
#	print(f"Цвет № {i}")


def colorLine(c, s):
    """
    c - цвет текста.
    s - строка которая быудет выводится между линиями со звездочками.
    Метод вывода теста приветствия.
    """
    os.system("cls")
    color(c)
    print("*" * (len(s) + 2))
    print(" " + s)
    print("*" * (len(s) + 2))

#colorLine(15, "Привет, я такой типа привлекаю внимание.")


def roulette():
    """
    Метод вывода меню Рулетки.
    """
    pass


def getRoulette(visible):
    """
    visible - (True or False) определяет делать ли паузу при вызове сменяющихся цифр на колесе рулетки (вкл/выкл анимации рулетки).
    Функция создания анимации рулетки и возвращающая выпавшее на колесе число.
    """
    pass


def dice():
    """
    Метод вывода меню Костей.
    """
    pass


def getDice():
    """
    Функция создания анимации костей и возвращает сумму выпавших граней.
    """
    pass


def oneHandBandit():
    """
    Метод вывода меню Однорукого бандита.
    """
    pass


def getOneHandBandit(stavka):
    """
    stavka - сумма, которую "поставил" игрок, в зависимости от которой будут начисляться  или вычитаться деньги.
    Функция отображения анимации однорукого бандита, символическое отображение слотов игрового автомата.
    """
    pass


def getMaxCount(digit, v1, v2, v3, v4, v5):
    """
    digit - число для сравнения.
    v1-v5 - индекс переменной означающий порядок цифры в случайно сгенерированном ряду.
    Функция, которая анализирует совпадения чисел.
    """
    pass


def getOneHandBanditRes():
    """
    Функция, которая расчитывает выигрыш или проигрыш пользователя.
    """
    pass


def win(result):
    """
    result - сумма выигранных средств.
    valuta - запись названия игровой валюты.
    money - показывает текущее количество денег у игрока.
    Метод выводящий текст при выигрыше.
    """
    color(14)
    print(f"    Победа за тобой! Выигрыш составляет: {result} {valuta}")
    print(f"    У тебя на счету: {money} {valuta}")


def fail(result):
    """
    result - сумма проигранных средств.
    valuta - запись названия игровой валюты.
    money - показывает текущее количество денег у игрока.
    Метод выводящий текст при проигрыше.
    """
    color(12)
    print(f"    К сожалению, проигрыш! {result} {valuta}")
    print(f"    У тебя на счету: {money} {valuta}")
    print("    Обязательно нужно отыграться!")

input()