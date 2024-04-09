import java.util.Scanner;

public class RightTriangle{

	public static void main(String[] args){

	Scanner scanner = new Scanner(System.in);

	System.out.print("Enter a number: ");
	
	int numberOfRows = scanner.nextInt();

	int i = 0;

	int j = 0;

	for(i= 0; i< numberOfRows; i++) {

	for(j= 0; j <= i; j++) {

	System.out.print(" *");

		}

	System.out.println();

	}

	}

}
	
