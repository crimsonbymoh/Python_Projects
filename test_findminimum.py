from find_minimum import minimum


def test_find_minimum():

	assert minimum([8,4,9,2,5,7,3]) == 2
	
	assert minimum([2.3,4.5,9.2,3.7,5.5,]) == 2.3

	assert minimum([-1,-4,-9,-2,-5,-7,]) == -9

	assert minimum([1,2,3,4,5,6,7]) == 1
	
	assert minimum([100,200,300,400,500,600,700]) == 100
	
	