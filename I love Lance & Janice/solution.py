def answer(s):
	return ''.join([chr(ord('z') - ord(letter) + ord('a')) if ord('a') <= ord(letter) <= ord('z') else letter for letter in s])
