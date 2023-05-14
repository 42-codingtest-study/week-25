package b5_10807;
import java.util.Scanner;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		int N = s.nextInt();
		int[] input = new int[N];
		for (int i = 0; i < N; i++) {
			input[i] = s.nextInt();			
		}
		int z = s.nextInt();
		int sum = 0;
		for (int i = 0; i < N; i++) {
			if (input[i] == z)
				sum += 1;
		}
		System.out.print(sum);
	}

}
