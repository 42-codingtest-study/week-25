package b4_2752;
import java.util.*;

public class Main {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		//int a = s.nextInt(), b = s.nextInt(), c = s.nextInt();
		List<Integer> obj =  new ArrayList<>(3);
		
		for(int i = 0; i < 3; i++) {
			obj.add(s.nextInt());
		}
		
		obj.sort(Comparator.naturalOrder());

		for(Integer x: obj) {
			System.out.printf(x+" ");
		}
	}

}
/*
System.out.println(obj);

obj.sort(Comparator.naturalOrder());
System.out.println(obj);
*/