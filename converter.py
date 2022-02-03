from colorama import Fore, Back, Style
from colorama import init

# инициализация библиотеки colorama
init(autoreset=True)

MENU = """
#####################################################################
#                                                                   #
#       Программа конвертер температур:                             #
#       Фаренгейт в Цельсий = F to C                                #
#       Цельсий в Фаренгейт = C to F                                #
#                                                                   #
#       Команды приложения:                                         #
#       c   -   конвертация температуры в градусы по Цельсию.       #
#       f   -   конвертация температуры в градусы по Фаренгейту.    #
#       e   -   выход из программы.                                 #
#                                                                   #
#####################################################################
"""
print(Fore.YELLOW + Style.BRIGHT + MENU)

while True:
	command = input("Введите Вашу команду: ")
	if command == 'c':
		temp_F = float(input("Введите градусы по Фаренгейту: "))
		temp_C = (temp_F - 32) * (5/9)
		temp_C = round(temp_C,1)
		print(Style.BRIGHT + Fore.RED + f'Температура по Цельсию: {temp_C}')
		print()

	elif command == 'f':
		temp_C = float(input("Введите градусы по Цельсию: "))
		temp_F = (temp_C * (9/5)) + 32
		temp_F = round(temp_F,1)
		print(Style.BRIGHT + Fore.BLUE + f'Температура по Фаренгейту: {temp_F}')
		print()

	elif command == 'e':
		break

	else:
		print('Введите правильную команду')
		print()