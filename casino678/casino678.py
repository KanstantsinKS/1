import os
import ctypes as ctp
import random as rnd


valuta = "руб"
money = 0
startMoney = 0
defaultMoney = 10000
playGame = True
ctp.windll.Kernel32.GetStdHandle.restype = ctp.c_ulong
h = ctp.windll.Kernel32.GetStdHandle(ctp.c_ulong(0xFFFFFFF5))


def main():
	"""
	Главный метод игры.
	"""
	global money, playGame
	money = loadMoney()
	startMoney = money
	while (playGame and money > 0):
		colorLine(10, "Приветствую тебя в нашем казино дружище!")
		color(14)
		print(f" У тебя на счету {money} {valuta}.")

		color(6)
		print("Ты можешь сыграть в:")
		print("    1. Рулетку")
		print("    2. Кости")
		print("    3. Однорукого бандита")
		print("    0. Выход. Ставка 0 в играх - выход.")
		color(7)

		x = getInput("0123", "    Твой выбор? ")
		if (x == "0"):
			playGame = False
		elif (x == "1"):
			roulette()
		elif (x == "2"):
			dice()
		elif (x == "3"):
			neHandBandit()

	colorLine(12, "Жаль, что ты покидаешь нас! Но возвращайся скорей!")
	color(13)
	if (money <= 0):
		print(" Упс, ты остался без денег. Возьми микрокредит и возвращайся!")

	color(11)
	if (money > startMoney):
		print(" Ну что же, поздравляем с прибылью!")
		print(f" На начало игры у тебя было всего {startMoney} {valuta}.")
		print(f" А сейчас у тебя {money} {valuta}! Ты выиграл целых {money - startMoney} {valuta}!")
	elif (money < startMoney):
		print(f" К сожалению, сегодня ты проиграл {startMoney - money} {valuta}...")
		print(" В следующий раз все обязательно получится!")
	else:
		print(f"К сожалению, сегодня ты не выиграл ничего... Зато ты остался при своих {money} {valuta}!")

	saveMoney(money)

	color(7)

	quit(0)


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
		moneyInFile = int(file.readline())
		file.close()
	except FileNotFoundError:
		print(f"Файла сохранения не существует, задано значение {defaultMoney} {valuta}.")
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
	playRoulette - отвечает за включение анимации рулетки.
	dozen - переменная для хранения выбора игрока в дюжине.
	dozenText - запоминает название выбранной дюжины.
	dozenWin - выпавшая дюжина (1 - 3).
	number - хранит выбранное игроком число.
	bet - ставка игрока.
	rouletteNumber - число выпавшее в рулетке.
	Метод вывода меню Рулетки.
	"""
	global money
	playGame = True # Маркер главного цикла рулетки.

	while (playGame and money > 0):
		colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ!")
		color(14)
		print(f"\n У тебя на счету {money} {valuta}\n")
		color(11)
		print(" Твоя ставка будет на...")
		print("     1. Чётное (выигрыш 1:1)")
		print("     2. Нечётное (выигрыш 1:1)")
		print("     3. Дюжина (выигрыш 3:1)")
		print("     4. Число (выигрыш 36:1)")
		print("     0. Возрат к выбору игры")

		x = getInput("01234", "     Твой выбор? ")

		playRoulette = True

		if (x == "3"):
			color(2)
			print()
			print(" Выбери числа...")
			print("     1. От 1 до 12")
			print("     2. От 13 до 24")
			print("     3. От 25 до 36")
			print("     0. Вернуться назад")

			dozen = getInput("0123", "     Твой выбор? ")

			if (dozen == "1"):
				dozenText = "От 1 до 12"
			elif (dozen == "2"):
				dozenText = "От 13 до 24"
			elif (dozen == "3"):
				dozenText = "От 25 до 36"
			elif (dozen == "0"):
				playRoulette = False
		elif (x == "4"):
			number = getIntInput(0, 36, "     На какое число ставишь? (0..36): ")

		color(7)
		if (x == "0"):
			return 0
		
		if (playRoulette):
			bet = getIntInput(0, money, f"     Сколько поставишь? (не больше {money}): ")
			if (bet == 0):
				return 0
			
			# Анимация рулетки и получение номера, False отключить анимацию.
			# rouletteNumber = getRoulette(True)
			rouletteNumber = rnd.randint(0, 38)

		print()
		color(11)
		if (rouletteNumber < 37):
			print(f"     Выпало число {rouletteNumber}! " + "*" * rouletteNumber)
		else:
			if (rouletteNumber == 37):
				printRouletteNumber = "00"
			elif (rouletteNumber == 38):
				printRouletteNumber = "000"
			print(f"     Выпало число {printRouletteNumber}! ")

		if (x == "1"):
			# Ставка на чётное.
			print("     Ты ставил на ЧЁТНОЕ!")
			if (rouletteNumber < 37 and rouletteNumber % 2 == 0):
				money += bet
				win(bet)
			else:
				money -= bet
				fail(bet)
		elif (x == "2"):
			# Ставка на нечётное.
			print("     Ты ставил на НЕЧЁТНОЕ!")
			if (rouletteNumber < 37 and rouletteNumber % 2 != 0):
				money += bet
				win(bet)
			else:
				money -= bet
				fail(bet)
		elif (x == "3"):
			# Ставка на дюжину.
			print(f"     Ставка сделана на диапазон чисел {dozenText}.")
			dozenWin = ""
			if (rouletteNumber > 0 and rouletteNumber < 13):
				dozenWin = "1"
			elif (rouletteNumber > 12 and rouletteNumber < 25):
				dozenWin = "2"
			elif (rouletteNumber > 24 and rouletteNumber < 37):
				dozenWin = "3"

			if (dozen == dozenWin):
				money += bet * 2
				win(bet * 3)
			else:
				money -= bet * 2
				fail(bet)
		elif (x == "4"):
			# Ставка на число.
			print(f"     Ставка сделана на число {number}!")
			if (rouletteNumber == number):
				money += bet * 35
				win(bet * 36)
			else:
				money -= bet
				fail(bet)

		print()
		input(" Нажми Enter для продолжения...")



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

main()