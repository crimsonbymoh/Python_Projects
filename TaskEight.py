totalCounter = 1;
multiple1 = 4;
totalCount = 1;
multiple2 = 8;
sumCounter = 0;
sumCount = 0;
sumTotal = 0;

for counter in range(5):
	totalCounter = totalCounter * multiple1 

	sumCounter = sumCounter + totalCounter

for counter1 in range(5):

	totalCount = totalCount * multiple2

	sumCount = sumCount + totalCount

sumTotal = sumCounter + sumCount

print(sumTotal, end= ' ')

