from find_longest_word import longest_word


def test_longest_word():

	words = ["welcome", "out", "weather", "mobile", "breakfast", "journey"]

	longest_word, max_length = longest_word(words)
	
	
	assert  longest_word == "breakfast" and max_length == "9"