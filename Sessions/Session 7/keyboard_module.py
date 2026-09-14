# Keyboard module for handling keyboard input and replacing characters in a string.


def fix_broken_keyboard(sentence):
	"""Replace the words used as placeholders for the broken keys."""
	return sentence.replace("not", "a").replace("poor", "u")
