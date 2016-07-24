import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

// works for sample cases

public class AFightToFinish {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		//System.out.println("Enter 3 ints");
		int noDiceHas = in.nextInt();
		int tiamatHp = in.nextInt();
		int threshold = in.nextInt();
		ArrayList<Integer> dice = new ArrayList<>();
		
		for (int k =0; k <noDiceHas; k++ ){
			Integer anInt = in.nextInt();
			dice.add(anInt);
		}
		
		if (dice.size() == 2) {
			int intA = dice.get(0);
			int intB = dice.get(1);
			
			if (intA + intB >= tiamatHp) {
				System.out.println("d" + intA + " " + "d" + intB);
			} else {
				System.out.println("WELL WE TRIED");
			}

		}
		
		Collections.sort(dice);	// sorts the array
		
		int lastNo = dice.get(dice.size()-1);
		int secondLastNo = dice.get(dice.size()-2);
		
		if (lastNo + secondLastNo < tiamatHp) {
			System.out.println("WELL WE TRIED");
		} else {
			
			boolean canSolve = false;
			int prev = dice.get(0);
			for (int j=1; j<dice.size(); j++) {
				int cur = dice.get(j);
				if (((prev+cur)/2) >= tiamatHp) {
					canSolve = true;
					System.out.println("d"+prev+" "+ "d"+cur);
					break;
				} else {}
			}
			
			if (!canSolve) {
				System.out.println("WELL WE TRIED");
			}
		}
				
				
		
			
		//for (Integer s: diceSplitInt) {
		//	System.out.println(s);
		//}
		
		

		
	}
}
