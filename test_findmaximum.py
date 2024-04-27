from find_maximum import maximum


def test_find_maximum():

	assert maximum([8,4,9,2,5,7,3]) == 9
	
	assert maximum([2.3,4.5,9.2,3.7,5.5,]) == 9.2

	assert maximum([-1,-4,-9,-2,-5,-7,]) == -1

	assert maximum([1,2,3,4,5,6,7]) == 7
	
	assert maximum([100,200,300,400,500,600,700]) == 700
	
	