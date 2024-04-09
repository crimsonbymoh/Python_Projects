import java.util.Scanner;

public class StudentScore{
	
	public static void main(String[] args){

	Scanner input = new Scanner(System.in);

	int passed = 0;

	int failed = 0;

	for (int i = 1; i <= 15; i++ ) {

	System.out.print("Enter Score For Student " + i + ": ");

			int score = input.nextInt();


			if (score >= 45){

			   passed++;

			}

			else {

			  failed++;

			  }

			}

	System.out.println("\nNumber Of Students That Passed: " + passed);

	System.out.println("\nNumber Of Students That Failed: " + failed);
	
	}


}