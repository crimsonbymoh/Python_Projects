from removeoddindex import remove_odd_index


def test_remove_odd_index():

	assert remove_odd_index("semicolon") == "eioo"
	assert remove_odd_index("Mohammed") == "oamd"
	assert remove_odd_index("Adedamola") == "ddml"
	assert remove_odd_index("Adedotun") == "aeou"
	
	




