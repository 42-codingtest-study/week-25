package b3_2490;
import java.util.*;
/*
 * ������ 4���� ������ ���� 0,1 �ν� �� 3ȸ ���� �� 5���� ����� ���� ����
 * 1�� ����(0~4)�� ���� ���������� -> ABCDE
 * ->3���� 4ĭ �迭�� ����� 1 ������ count �ϴ� �˰��� => �׳� sum���� ���ϱ�
 * ->switch������ 5�� �� �ϳ� ���  
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
