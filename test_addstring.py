from add_ing_to_string import add_string


def test_add_string():

	assert add_string("abc") == 'abcing'
	assert add_string("string") ==  'stringly'
	
	assert add_string("on") == 'on'