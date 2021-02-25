import os
import ctypes as ctp
import time
import random as rnd


currency = "руб"
money = 0
start_money = 0
default_money = 10000
play_game = True
ctp.windll.Kernel32.GetStdHandle.restype = ctp.c_ulong
h = ctp.windll.Kernel32.GetStdHandle(ctp.c_ulong(0xFFFFFFF5))


def get_input(digit, message):
	"""
	digit - возможные для ввода значения в формате строки 0123.
	message - строка-приглашения при входе.
	ret - введенный пользователем симол.
	Функция ввода значения.
	"""
	color(7)
	ret = ""
	while ret == "" or ret not in digit:
		ret = input(message)
	return ret


def get_int_input(minimum, maximum, message):
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
	while ret < minimum or ret > maximum:
		st = input(message)
		if st.isdigit():
			ret = int(st)
		else:	
			print(" Введи целое число! ")
	return ret


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
	Метод записывает сумму средств игрока из аргумента moneyToSave в файл money.dat.
	"""
	try:
		file = open("money.dat", "w")
		file.write(str(money_to_save))
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


def color_line(c, s):
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


def get_roulette(visible):
	"""
	visible - (True or False) делать ли паузу при вызове сменяющихся цифр на колесе рулетки (вкл/выкл анимации рулетки).
	tick_time - время в секундах, на которое увеличивается пауза за одну итерацию цикла (тип double).
	main_time - пауза в секундах (тип double).
	number - номер выпавший в рулетке.
	increase_tick_time - время в секундах, на которое увеличивается tickTime для создания эффекта неравномерности паузы.
	col - цвел выводимого сообщения.
	Функция создания анимации рулетки и возвращающая выпавшее на колесе число.
	"""
	tick_time = rnd.randint(100, 200) / 10000
	main_time = 0
	number = rnd.randint(0, 38)
	increase_tick_time = rnd.randint(100, 110) / 100
	col = 1

	# Цикл анимацмм.
	while main_time < 0.7:
		
		# Изменение цвета.
		col += 1
		if col > 15:
			col = 1

		# Увеличение времени паузы.
		main_time += tick_time
		tick_time *= increase_tick_time

		# Увеличение номера и вывод на экран.
		color(col)
		number += 1
		if number > 38:
			number = 0
			
		# Алгоритм обработки скрытых чисел 37 и 38, соответственно "00" и "000"
		print_number = number
		if number == 37:
			print_number = "00"
		elif number == 38:
			print_number = "000"

		# Вывод на экран сообщения.
		print(" Число >>>>", print_number)

		# Делаем паузу.
		if visible:
			time.sleep(main_time)
	
	# Возвращаем число выпавшее в рулетке.
	return number


def print_roulette():
	"""
	Метод отрисовывает поле рулетки.
	"""
	print(
		"-----" * 13 + "\n"
		+ "|    |  3 |  6 |  9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 |\n"
		+ "     " + "-----" * 12 + "\n"
		+ "|  0 |  2 |  5 |  8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 35 | 35 |\n"
		+ "     " + "-----" * 12 + "\n"
		+ "|    |  1 |  4 |  7 | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 34 | 34 |\n"
		+ "-----" * 13 + "\n"
		+ "     |       1ST 12      |       2ND 12      |       3RD 12      |\n"
		+ "     " + "-----" * 12 + "\n"
		+ "                 |       ЧЁТНОЕ      |     НЕЧЁТНОЕ     |\n"
		+ "                 "+"-----" * 8 + "\n"
	)


def roulette():
	"""
	play_roulette - отвечает за включение анимации рулетки.
	dozen - переменная для хранения выбора игрока в дюжине.
	dozen_text - запоминает название выбранной дюжины.
	dozen_win - выпавшая дюжина (1 - 3).
	number - хранит выбранное игроком число.
	bet - ставка игрока.
	roulette_number - число выпавшее в рулетке.
	Метод вывода меню Рулетки.
	"""
	global money
	play_game = True  # Маркер главного цикла рулетки.

	while play_game and money > 0:
		
		color_line(3, " ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ! ")
		color(14)
		print(f"\n У тебя на счету {money} {currency}\n")
		print_roulette()
		color(11)
		print(" Твоя ставка будет на...")
		print(" 1. Чётное (выигрыш 1:1)")
		print(" 2. Нечётное (выигрыш 1:1)")
		print(" 3. Дюжина (выигрыш 3:1)")
		print(" 4. Число (выигрыш 36:1)")
		print(" 0. Возрат к выбору игры")

		x = get_input("01234", " Твой выбор? ")

		play_roulette = True

		if x == "3":
			color(2)
			print()
			print(" Выбери числа...")
			print(" 1. От 1 до 12")
			print(" 2. От 13 до 24")
			print(" 3. От 25 до 36")
			print(" 0. Вернуться назад")

			dozen = get_input("0123", " Твой выбор? ")

			if dozen == "1":
				dozen_text = "от 1 до 12"
			elif dozen == "2":
				dozen_text = "от 13 до 24"
			elif dozen == "3":
				dozen_text = "от 25 до 36"
			elif dozen == "0":
				play_roulette = False
		elif x == "4":
			number = get_int_input(0, 36, " На какое число ставишь? (0..36): ")

		color(7)
		if x == "0":
			return 0
		
		if play_roulette:
			bet = get_int_input(0, money, f" Сколько поставишь? (не больше {money} {currency}): ")
			if bet == 0:
				return 0
			
			# Анимация рулетки и получение номера, False отключить анимацию.
			roulette_number = get_roulette(True)

		print()
		color(11)

		if roulette_number < 37:
			print(f" Выпало число {roulette_number}! " + "*" * roulette_number)
		else:
			if roulette_number == 37:
				print_roulette_number = "00"
			elif roulette_number == 38:
				print_roulette_number = "000"
			print(f" Выпало число {print_roulette_number}! ")

		if x == "1":
			
			# Ставка на чётное.
			print(" Ты ставил на ЧЁТНОЕ!")
			if roulette_number < 37 and roulette_number % 2 == 0:
				money += bet
				win(bet)
			else:
				money -= bet
				fail(bet)
		elif x == "2":
			
			# Ставка на нечётное.
			print(" Ты ставил на НЕЧЁТНОЕ!")
			if roulette_number < 37 and roulette_number % 2 != 0:
				money += bet
				win(bet)
			else:
				money -= bet
				fail(bet)
		elif x == "3":
			
			# Ставка на дюжину.
			print(f" Ставка сделана на диапазон чисел {dozen_text}.")
			dozen_win = ""
			if roulette_number > 0 and roulette_number < 13:
				dozen_win = "1"
			elif roulette_number > 12 and roulette_number < 25:
				dozen_win = "2"
			elif roulette_number > 24 and roulette_number < 37:
				dozen_win = "3"

			if dozen == dozen_win:
				money += bet * 2
				win(bet * 3)
			else:
				money -= bet * 2
				fail(bet)
		elif x == "4":
			
			# Ставка на число.
			print(f" Ставка сделана на число {number}!")
			if roulette_number == number:
				money += bet * 35
				win(bet * 36)
			else:
				money -= bet
				fail(bet)

		print()
		input(" Нажми Enter для продолжения...")


def get_dice():
	"""
	count - сколько раз будут перекатываться кости.
	sleep - отвечает за паузу при смене кубиков. 
	Функция создания анимации костей и возвращает сумму выпавших граней.
	"""
	count = rnd.randint(3, 8)
	sleep = 0
	while count > 0:
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
	play_round - логическая, отвечает за игровой цикл выбрасывания и подсчета результата граней.
	first_play - логическая, определяет первый это раунд или нет. При выходе определяет проиграет или получит игрок.
	control - запоминает размер ставки игрока, которая списывается в случае проиграша.
	old_result - хранит сумму граней костей прошлой игры, для определение выигрыша или проигрыша при сравнении.
	dice_result - текущая сумма граней костей.
	bet - ставка игрока.
	Метод вывода интерфейса Костей. В методе организуется ставка и вызывается анимация getDice().
	"""
	global money
	play_game = True

	# Главный цикл Костей.
	while play_game:
		
		print()
		color_line(3, " ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В КОСТИ! ")
		color(14)
		print(f"\n У тебя на счету {money} {currency}\n")
		
		color(7)
		bet = get_int_input(0, money, f" Сделай ставку в пределах {money} {currency}: ")
		if bet == 0:
			return 0

		play_round = True
		control = bet
		old_result = get_dice()
		first_play = True

		while play_round and bet > 0 and money > 0:
			
			if bet > money:
				bet = money

			color(11)
			print(f" В твоём распоряжении {bet} {currency}. ")
			color(12)
			print(f" Текущая сумма чисел на костях: {old_result}. ")
			color(11)
			print(" Сумма чисел на гранях будет больше, меньше или равна предыдущей? ")
			color(7)
			x = get_input("0123", " Введи 1 - больше, 2 - меньше, 3 - равно, 0 - выход: ")

			if x != "0":
				first_play = False
				if bet > money:
					bet = money
				
				money -= bet
				dice_result = get_dice()

				win_round = old_result > dice_result and x == "2" or old_result < dice_result and x == "1"

				if not x == "3":
					if win_round:
						money += bet + bet // 5
						win(bet // 5)
						bet += bet // 5
					else:
						bet = control
						fail(bet)
				elif x == "3":
					if old_result == dice_result:
						money += bet * 3
						win(bet * 2)
						bet *= 3
					else:
						bet = control
						fail(bet)
			
				old_result = dice_result

			else:
				# При выходе на первой итерации.
				if first_play:
					money -= bet
				play_round = False


def one_hand_bandit():
	"""
	Метод вывода меню Однорукого бандита.
	"""
	global money
	play_game = True

	while play_game:
		color_line(3 , " ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В ОДНОРУКОГО БАНДИТА! ")
		color(14)
		print(f"\n У тебя на счету {money} {currency}.\n")
		color(5)
		print(" Правила игры: ")
		print(" 1. При совпадении 2-х чисел ставка не списывается. ")
		print(" 2. При совпадении 3-х чисел выигрыш 2:1. ")
		print(" 3. При совпадении 4-х чисел выигрыш 5:1. ")
		print(" 4. При совпадении 5-ти чисел выигрыш 10:1. ")
		print(" Ставка 0 для завершения игры.\n")

		bet = get_int_input(0, money ,f" Сделай ставку от 0 до {money} {currency}: ")
		if bet == 0:
			return 0

		money -= bet
		money += get_one_hand_bandit_res(bet)

		if money <= 0:
			play_game = False


def get_max_count(digit, v1, v2, v3, v4, v5):
	"""
	digit - число для сравнения.
	v1-v5 - индекс переменной означающий порядок цифры в случайно сгенерированном ряду.
	Функция, которая анализирует совпадения чисел.
	"""
	ret = 0
	if digit == v1:
		ret =+ 1
	if digit == v2:
		ret += 1
	if digit == v3:
		ret += 1
	if digit == v4:
		ret += 1
	if digit == v5:
		ret += 1
	return ret



def get_one_hand_bandit_res(bet):
	"""
	Функция, которая расчитывает выигрыш или проигрыш пользователя.
	"""
	res = bet
	d1 = 0
	d2 = 0
	d3 = 0
	d4 = 0
	d5 = 0
	get_d1 = True
	get_d2 = True
	get_d3 = True
	get_d4 = True
	get_d5 = True
	col = 10
	while get_d1 or get_d2 or get_d3 or get_d4 or get_d5:

		if get_d1:
			d1 += 1
		if get_d2:
			d2 -= 1
		if get_d3:
			d3 += 1
		if get_d4:
			d4 -= 1
		if get_d5:
			d5 += 1

		if d1 > 9:
			d1 = 0
		if d2 < 0:
			d2 = 9
		if d3 > 9:
			d3 = 0
		if d4 < 0:
			d4 = 9
		if d5 > 9:
			d5 = 0

		if rnd.randint(0, 20) == 1:
			get_d1 = False
		if rnd.randint(0, 20) == 1:
			get_d2 = False
		if rnd.randint(0, 20) == 1:
			get_d3 = False
		if rnd.randint(0, 20) == 1:
			get_d4 = False
		if rnd.randint(0, 20) == 1:
			get_d5 = False

		time.sleep(0.1)
		color(col)
		col += 1
		if col > 15:
			col = 10

		print(" " + "%" * 10)
		print(f" {d1} {d2} {d3} {d4} {d5} ")

	max_count = get_max_count(d1, d1, d2, d3, d4, d5)

	if max_count < get_max_count(d2, d1, d2, d3, d4, d5):
		max_count = get_max_count(d2, d1, d2, d3, d4, d5)
	if max_count < get_max_count(d3, d1, d2, d3, d4, d5):
		max_count = get_max_count(d3, d1, d2, d3, d4, d5)
	if max_count < get_max_count(d4, d1, d2, d3, d4, d5):
		max_count = get_max_count(d4, d1, d2, d3, d4, d5)
	if max_count < get_max_count(d5, d1, d2, d3, d4, d5):
		max_count = get_max_count(d5, d1, d2, d3, d4, d5)

	color(14)
	if max_count == 2:
		print(f" Совпадение 2-х чисел! Твой выигрыш равен размеру ставки: {res}")
	elif max_count == 3:
		res *= 2
		print(f" Совпадение 3-х чисел! Твой выигрыш 2:1 составляет: {res}")
	elif max_count == 4:
		res *= 5
		print(f" Совпадение 4-х чисел! Твой выигрыш 5:1 составляет: {res}")
	elif max_count == 5:
		res *= 10
		print(f" Совпадение 5-х чисел! Твой выигрыш 10:1 составляет: {res}")
	else:
		fail(res)
		res = 0

	color(11)
	print()
	input(" Нажми Enter, чтобы продолжить... ")
	return res


def win(result):
	"""
	result - сумма выигранных средств.
	currency - запись названия игровой валюты.
	money - показывает текущее количество денег у игрока.
	Метод выводящий текст при выигрыше.
	"""
	color(14)
	print(f" Победа за тобой! Выигрыш составляет: {result} {currency}")
	print(f" У тебя на счету: {money} {currency}")


def fail(result):
	"""
	result - сумма проигранных средств.
	currency - запись названия игровой валюты.
	money - показывает текущее количество денег у игрока.
	Метод выводящий текст при проигрыше.
	"""
	color(12)
	print(f" К сожалению, проигрыш! {result} {currency}")
	print(f" У тебя на счету: {money} {currency}")
	print(" Обязательно нужно отыграться!")


def main():
	"""
	Главный метод игры.
	"""
	global money, play_game
	money = load_money()
	start_money = money
	while play_game and money > 0:
		color_line(10, " Приветствую тебя в нашем казино дружище! ")
		color(14)
		print(f" У тебя на счету {money} {currency}.")

		color(6)
		print(" Ты можешь сыграть в:")
		print(" 1. Рулетку")
		print(" 2. Кости")
		print(" 3. Однорукого бандита")
		print(" 0. Выход. Ставка 0 в играх - выход.")
		color(7)

		x = get_input("0123", " Твой выбор? ")
		if x == "0":
			play_game = False
		elif x == "1":
			roulette()
		elif x == "2":
			dice()
		elif x == "3":
			one_hand_bandit()

	color_line(12, " Жаль, что ты покидаешь нас! Но возвращайся скорей! ")
	color(13)
	if money <= 0:
		print(" Упс, ты остался без денег. Возьми микрокредит и возвращайся!")

	color(11)
	if money > start_money:
		print(" Ну что же, поздравляем с прибылью!")
		print(f" На начало игры у тебя было всего {start_money} {currency}.")
		print(f" А сейчас у тебя {money} {currency}! Ты выиграл целых {money - start_money} {currency}!")
	elif money < start_money:
		print(f" К сожалению, сегодня ты проиграл {start_money - money} {currency}...")
		print(" В следующий раз все обязательно получится!")
	else:
		print(f" К сожалению, сегодня ты не выиграл ничего... Зато ты остался при своих {money} {currency}!")

	save_money(money)

	color(7)

	quit(0)


main()
