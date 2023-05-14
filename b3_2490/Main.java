package b3_2490;
import java.util.*;
/*
 * 윷가락 4개의 정보가 각각 0,1 로써 총 3회 들어올 때 5가지 경우의 수를 만듦
 * 1의 개수(0~4)에 따라 도개걸윷모 -> ABCDE
 * ->3개의 4칸 배열을 만들고 1 개수로 count 하는 알고리즘 => 그냥 sum에서 더하기
 * ->switch문으로 5개 중 하나 출력  
 */
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner(System.in);
		for(int i = 0; i < 3; i++) {
			int sum = 0;
			for (int j = 0; j < 4; j++) {
				int n = s.nextInt();
				sum += n;
			}
			switch(sum) {
			case 0:
				System.out.println("D");
				break;
			case 1:
				System.out.println("C");
				break;
			case 2:
				System.out.println("B");
				break;
			case 3:
				System.out.println("A");
				break;
			case 4:
				System.out.println("E");
				break;
			
			}

		}
		
	}

}
