# TDD - Test Driven Development
from random import choice


def greet(name, isEnemy):
	if not isinstance(isEnemy, bool):
		raise ValueError('isEnemy must be boolean type')
	if isEnemy:
		return f'Hello {name}! I will kill you!'
	else:
		return f'Hello {name}! How are you?'

def eat_burgers(number):
	if number > 3:
		return 'Oh! I overate!'
	else:
		return 'Mmm! That was excellent'


def can_fly(name):
	if name == 'Batman':
		return f'{name} have to be able to fly'
	else:
		return 'Anyone else have to be able to fly'


def get_arsenal():
	return choice(('knife', 'handgun', 'machin gun'))


