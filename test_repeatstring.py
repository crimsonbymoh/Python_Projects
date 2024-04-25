
from repeatstring import repeat_string


def test_repeat_string():

	assert repeat_string("hello", 3) == "hellohellohello"
	assert repeat_string("hi", 4.5) == "hi"
	assert repeat_string("hi", 4.5) == "hihihihi"
	assert repeat_string("welcome", 3) == "welcomewelcomewelcome"
	assert repeat_string("welcome", 2.5) == "welcomewelcomewelcome"
	
	
	
	
	






# Test cases
print  # Output: 
print(repeat_string)    # Output: 'hi'