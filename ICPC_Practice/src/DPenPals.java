import java.util.HashMap;
import java.util.Scanner;

// correct :D 

public class DPenPals {
	private static HashMap<Integer, String> permutationMap = new HashMap<>();
	private static HashMap<String, Integer> alphabetMap = new HashMap<>();
	
	public static void main (String[] args) {
		solve();	
	}
	
	public static void solve() {
		Scanner in = new Scanner(System.in);
		// white space tab, in, space
        //System.out.println("enter permutation: ");

		String inPermutation = in.nextLine();
				//"qwdyrelukjaosphfginzxcvbtm";
				//in.nextLine();
        //System.out.println("enter msg: ");

		String inMsg = in.nextLine();
		//"or gdsck";
		//in.nextLine();
		
		Integer counter = 0;

		String alphabet = "abcdefghijklmnopqrstuvwxyz";
		for (char ch: alphabet.toCharArray() ) {
			alphabetMap.put(Character.toString(ch), counter);
			counter ++;
		}
		
		Integer counter2 = 0;
		for (char ch: inPermutation.toCharArray()) {
			permutationMap.put(counter2, Character.toString(ch));
			counter2 ++;
		}
		
		String output = "";
		for (int i=0; i<inMsg.length(); i++) {
			if (Character.toString(inMsg.charAt(i)).equals(" ")) {
				output += " ";
				} 
			else {
		
				Integer anInt = alphabetMap.get(Character.toString(inMsg.charAt(i)));
				String msgPart = permutationMap.get(anInt);
				output += msgPart;
			}
		}
	
		System.out.println(output);
		
			
		
	}
}
