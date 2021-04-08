# unittest - python module with unit tasting framework
import unittest
import upper


class TestUpper(unittest.TestCase):
	def test_one_word(self):
		text = 'hello!'
		result = upper.upper_text(text)
		self.assertEqual(result, 'Hello!')
		self.assertNotEqual(result, 'hello!')


	def test_multiple_words(self):
		text = 'hello world!'
		result = upper.upper_text(text)
		self.assertEqual(result, 'Hello World!')


if __name__ == '__main__':
	unittest.main()




