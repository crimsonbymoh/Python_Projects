from largestnumber import largest,smallest


def test_for_largest_number():
	assert largest(13, 12, 19) == 19

	assert largest(3.5, 4.9, 7) == 7

	assert largest(-1, -4, -9) == -1



def test_for_smallest_number():
	assert smallest(4, 6, 10) == 4

	assert smallest(2.5, 3.7, 5) == 2.5

	assert smallest(-1, -4, -9) == -9



