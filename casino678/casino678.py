import os
import ctypes as ctp
import time
import random as rnd


valuta = "руб"
money = 0
startMoney = 0
defaultMoney = 10000
playGame = True
ctp.windll.Kernel32.GetStdHandle.restype = ctp.c_ulong
h = ctp.windll.Kernel32.GetStdHandle(ctp.c_ulong(0xFFFFFFF5))


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
			print(" Введи целое число! ")
	return ret


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
		print(f" Файла сохранения не существует, задано значение {defaultMoney} {valuta}.")
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
		print(" Ошибка создания файла, наше казино закрывается!")
		quit(0)

def color(c):
	"""
	с - номер цвета для установки.
	Метод установки цвета текста в консоли.
	"""
	ctp.windll.Kernel32.SetConsoleTextAttribute(h, c)


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


def getRoulette(visible):
	"""
	visible - (True or False) определяет делать ли паузу при вызове сменяющихся цифр на колесе рулетки (вкл/выкл анимации рулетки).
	tickTime - время в секундах, на которое увеличивается пауза за одну итерацию цикла (тип double).
	mainTime - пауза в секундах (тип double).
	number - номер выпавший в рулетке.
	increaseTickTime - время в секундах, на которое увеличивается tickTime для создания эффекта неравномерности паузы.
	col - цвел выводимого сообщения.
	Функция создания анимации рулетки и возвращающая выпавшее на колесе число.
	"""
	tickTime = rnd.randint(100, 200) / 10000
	mainTime = 0
	number = rnd.randint(0, 38)
	increaseTickTime = rnd.randint(100, 110) / 100
	col = 1

	# Цикл анимацмм.
	while (mainTime < 0.7):
		
		# Изменение цвета.
		col += 1
		if (col > 15):
			col = 1

		# Увеличение времени паузы.
		mainTime += tickTime
		tickTime *= increaseTickTime

		# Увеличение номера и вывод на экран.
		color(col)
		number += 1
		if (number > 38):
			number = 0
			
		# Алгоритм обработки скрытых чисел 37 и 38, соответственно "00" и "000"
		printNumber = number
		if (number == 37):
			printNumber = "00"
		elif (number == 38):
			printNumber = "000"

		# Вывод на экран сообщения.
		print(" Число >>>>", printNumber)

		# Делаем паузу.
		if (visible):
			time.sleep(mainTime)
	
	# Возвращаем число выпавшее в рулетке.
	return number


def printRoulette():
	"""
	Метож отрисовывает поле рулетки.
	"""
	print("-----" * 13 + "\n"
		+ "|    |  3 |  6 |  9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 |\n"
		+ "     " + "-----" * 12 + "\n"
		+ "|  0 |  2 |  5 |  8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 35 | 35 |\n"
		+ "     " + "-----" * 12 + "\n"
		+ "|    |  1 |  4 |  7 | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 34 | 34 |\n"
		+ "-----" * 13 + "\n"
		+ "     |       1ST 12      |       2ND 12      |       3RD 12      |\n"
		+ "     " + "-----" * 12 + "\n"
		+ "                 |       ЧЁТНОЕ      |     НЕЧЁТНОЕ     |\n"
		+ "                 "+"-----" * 8 + "\n")


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
		
		colorLine(3, " ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ! ")
		color(14)
		print(f"\n У тебя на счету {money} {valuta}\n")
		printRoulette()
		color(11)
		print(" Твоя ставка будет на...")
		print(" 1. Чётное (выигрыш 1:1)")
		print(" 2. Нечётное (выигрыш 1:1)")
		print(" 3. Дюжина (выигрыш 3:1)")
		print(" 4. Число (выигрыш 36:1)")
		print(" 0. Возрат к выбору игры")

		x = getInput("01234", " Твой выбор? ")

		playRoulette = True

		if (x == "3"):
			color(2)
			print()
			print(" Выбери числа...")
			print(" 1. От 1 до 12")
			print(" 2. От 13 до 24")
			print(" 3. От 25 до 36")
			print(" 0. Вернуться назад")

			dozen = getInput("0123", " Твой выбор? ")

			if (dozen == "1"):
				dozenText = "от 1 до 12"
			elif (dozen == "2"):
				dozenText = "от 13 до 24"
			elif (dozen == "3"):
				dozenText = "от 25 до 36"
			elif (dozen == "0"):
				playRoulette = False
		elif (x == "4"):
			number = getIntInput(0, 36, " На какое число ставишь? (0..36): ")

		color(7)
		if (x == "0"):
			return 0
		
		if (playRoulette):
			bet = getIntInput(0, money, f" Сколько поставишь? (не больше {money}): ")
			if (bet == 0):
				return 0
			
			# Анимация рулетки и получение номера, False отключить анимацию.
			rouletteNumber = getRoulette(True)

		print()
		color(11)
		if (rouletteNumber < 37):
			print(f" Выпало число {rouletteNumber}! " + "*" * rouletteNumber)
		else:
			if (rouletteNumber == 37):
				printRouletteNumber = "00"
			elif (rouletteNumber == 38):
				printRouletteNumber = "000"
			print(f" Выпало число {printRouletteNumber}! ")

		if (x == "1"):
			
			# Ставка на чётное.
			print(" Ты ставил на ЧЁТНОЕ!")
			if (rouletteNumber < 37 and rouletteNumber % 2 == 0):
				money += bet
				win(bet)
			else:
				money -= bet
				fail(bet)
		elif (x == "2"):
			
			# Ставка на нечётное.
			print(" Ты ставил на НЕЧЁТНОЕ!")
			if (rouletteNumber < 37 and rouletteNumber % 2 != 0):
				money += bet
				win(bet)
			else:
				money -= bet
				fail(bet)
		elif (x == "3"):
			
			# Ставка на дюжину.
			print(f" Ставка сделана на диапазон чисел {dozenText}.")
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
			print(f" Ставка сделана на число {number}!")
			if (rouletteNumber == number):
				money += bet * 35
				win(bet * 36)
			else:
				money -= bet
				fail(bet)

		print()
		input(" Нажми Enter для продолжения...")


def getDice():
	"""
	count - сколько раз будут перекатываться кости.
	sleep - отвечает за паузу при смене кубиков. 
	Функция создания анимации костей и возвращает сумму выпавших граней.
	"""
	count = rnd.randint(3, 8)
	sleep = 0
	while (count > 0):
		color(count + 7)
		x = rnd.randint(1, 6)
		y = rnd.randint(1, 6)
		print(" " * 10, "----- -----")
		print(" " * 10, f"| {x} | | {y} |")
		print(" " * 10, "----- -----")
		time.sleep(sleep)
		sleep += 1 / count
		count -= 1
	return x + y


def dice():
	"""
	playRound - логическая переменная отвечает за игровой цикл выбрасывания и подсчета результата граней.
	firstPlay - логическая переменная, определяет первый это раунд или нет. При выходе из игры определяет сколько проиграет или получит игрок.
	control - запоминает размер ставки игрока, которая списывается в случае проиграша.
	oldResult - хранит сумму граней костей прошлой игры, для определение выигрыша или проигрыша при сравнении.
	diceResult - текущая сумма граней костей.
	bet - ставка игрока.
	Метод вывода интерфейса Костей. В методе организуется ставка и вызывается анимация getDice().
	"""
	global money
	playGame = True

	# Главный цикл Костей.
	while (playGame):
		
		print()
		colorLine(3, " ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В КОСТИ! ")
		color(14)
		print(f"\n У тебя на счету {money} {valuta}\n")
		
		color(7)
		bet = getIntInput(0, money, f" Сделай ставку в пределах {money} {valuta}: ")
		if (bet == 0):
			return 0

		playRound = True
		control = bet
		oldResult = getDice()
		firstPlay = True

		while (playRound and bet > 0 and money > 0):
			
			if (bet > money):
				bet = money

			color(11)
			print(f" В твоём распоряжении {bet} {valuta}. ")
			color(12)
			print(f" Текущая сумма чисел на костях: {oldResult}. ")
			color(11)
			print(" Сумма чисел на гранях будет больше, меньше или равна предыдущей? ")
			color(7)
			x = getInput("0123", " Введи 1 - больше, 2 - меньше, 3 - равно, 0 - выход: ")

			if (x != "0"):
				firstPlay = False
				if (bet > money):
					bet = money
				
				money -= bet
				diceResult = getDice()

				winRound = (oldResult > diceResult and x == "2") or (oldResult < diceResult and 	x == "1")

				if (not x == "3"):
					if (winRound):
						money += bet + bet // 5
						win(bet // 5)
						bet += bet // 5
					else:
						bet = control
						fail(bet)
				elif (x == "3"):
					if (oldResult == diceResult):
						money += bet * 3
						win(bet * 2)
						bet *= 3
					else:
						bet = control
						fail(bet)
			
				oldResult = diceResult

			else:
				# При выходе на первой итерации.
				if (firstPlay):
					money -= bet
				playRound = False


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
	print(f" Победа за тобой! Выигрыш составляет: {result} {valuta}")
	print(f" У тебя на счету: {money} {valuta}")


def fail(result):
	"""
	result - сумма проигранных средств.
	valuta - запись названия игровой валюты.
	money - показывает текущее количество денег у игрока.
	Метод выводящий текст при проигрыше.
	"""
	color(12)
	print(f" К сожалению, проигрыш! {result} {valuta}")
	print(f" У тебя на счету: {money} {valuta}")
	print(" Обязательно нужно отыграться!")


def main():
	"""
	Главный метод игры.
	"""
	global money, playGame
	money = loadMoney()
	startMoney = money
	while (playGame and money > 0):
		colorLine(10, " Приветствую тебя в нашем казино дружище! ")
		color(14)
		print(f" У тебя на счету {money} {valuta}.")

		color(6)
		print(" Ты можешь сыграть в:")
		print(" 1. Рулетку")
		print(" 2. Кости")
		print(" 3. Однорукого бандита")
		print(" 0. Выход. Ставка 0 в играх - выход.")
		color(7)

		x = getInput("0123", " Твой выбор? ")
		if (x == "0"):
			playGame = False
		elif (x == "1"):
			roulette()
		elif (x == "2"):
			dice()
		elif (x == "3"):
			neHandBandit()

	colorLine(12, " Жаль, что ты покидаешь нас! Но возвращайся скорей! ")
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
		print(f" К сожалению, сегодня ты не выиграл ничего... Зато ты остался при своих {money} {valuta}!")

	saveMoney(money)

	color(7)

	quit(0)


main()