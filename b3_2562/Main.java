package b3_2562;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner (System.in);
		int max = 0, idx = 0;
		for(int i = 1; i <= 9; i++) { 
			int n = s.nextInt();
			if(n > max) {
				max = n;
				idx = i;
			}
		}
		System.out.printf("%d\n%d", max, idx);
	}

}
