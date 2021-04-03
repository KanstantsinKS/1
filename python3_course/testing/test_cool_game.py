import unittest
import cool_game


class CoolGameTest(unittest.TestCase):


	def test_greet(self):
		"""greet() have to return 'How are you?' If isEnemy == False"""
		self.assertEqual(cool_game.greet('Jack', False), 'Hello Jack! How are you?')


	def test_greet_enemy(self):
		"""greet() have to return 'I will kill you!' If isEnemy == True"""
		self.assertEqual(cool_game.greet('Ivan', True), 'Hello Ivan! I will kill you!')


	def test_greet_enemy_boolean(self):
		"""greet() have to return 'I will kill you!' If isEnemy == True"""
		with self.assertRaises(ValueError):
			cool_game.greet('Ivan', 'Bla')


	def test_eat_burgers(self):
		"""eat_burgers() have to return 'Mmm! That was excellent' If number =< 3"""
		self.assertEqual(cool_game.eat_burgers(3), 'Mmm! That was excellent')


	def test_eat_too_much_burgers(self):
		"""eat_burgers() have to return 'Oh! I overate!' If number > 3"""
		self.assertEqual(cool_game.eat_burgers(4), 'Oh! I overate!')


	def test_can_fly(self):
		"""can_fly() have to return 'Batman have to be able to fly' if name == 'Batman'"""
		self.assertTrue(cool_game.can_fly('Batman'), 'Batman have to be able to fly')


	def test_can_not_fly(self):
		"""can_fly() have to return 'Anyone else have to be able to fly' if name != 'Batman'"""
		self.assertEqual(cool_game.can_fly('Bob'), 'Anyone else have to be able to fly')
		self.assertEqual(cool_game.can_fly('Tim'), 'Anyone else have to be able to fly')
		self.assertEqual(cool_game.can_fly('Joe'), 'Anyone else have to be able to fly')


	def test_get_arsenal(self):
		self.assertIn(cool_game.get_arsenal(), ('knife', 'handgun', 'machin gun'))


if __name__ == '__main__':
	unittest.main()