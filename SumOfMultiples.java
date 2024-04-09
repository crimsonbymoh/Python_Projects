public class SumOfMultiples{

	public static void main(String[] args){

	int sum = 0;

	for (int i = 1; i <= 20000; i++) {

	  if (i % 10 == 0)

		sum += i;

		}

	System.out.print("The Sum of multiples of 10 Between 1 and 20000 is: " + sum);

	}


}


	

