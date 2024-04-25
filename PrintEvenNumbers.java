import java.util.Scanner;

	public class PrintEvenNumbers{

	public static void main(String[] args){

	Scanner scanner = new Scanner(System.in);

	int number = 100;

	for (int i = 1; i <= number; i++) {

	if (i % 2 == 0) {

	System.out.print(i + " ");
	
	  }

	}


	}
}

