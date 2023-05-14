package b2_2577;
import java.util.*;
public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s = new Scanner (System.in);
		int a = s.nextInt(), b = s.nextInt(), c = s.nextInt();
		
		String str = Integer.toString(a*b*c);
		HashMap<Character, Integer> map = new HashMap<>();
		
		for(int i = 0; i < 10; i++) {
			
			map.put((char)(i+'0'), 0);
		}
		for(char ch : str.toCharArray()) {
			if(map.containsKey(ch))
				map.put(ch, map.get(ch) + 1);
			
		}
		ArrayList<Character> keyList = new ArrayList<>(map.keySet());
		Collections.sort(keyList);
		for(char ch : keyList) {
			//System.out.println(ch);
			System.out.println(map.get(ch));
		}
	}

}
