import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Excellence {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int noStu = in.nextInt();
		
		ArrayList<Integer> ranks = new ArrayList<>();
		
		for (int i=0; i<noStu; i++) {
			Integer aRank = in.nextInt();
			ranks.add(aRank);
		}
		Collections.sort(ranks);
		// middle values
		int upperMid = noStu/2;
		int lowerMid = upperMid-1;
		int maxValue = ranks.get(lowerMid) + ranks.get(upperMid);
		
		int min = maxValue;
		int bkcounter = ranks.size()-1;
		
		for (int k=0; k<ranks.size()/2; k++) {
			int v1 = ranks.get(k);
			int v2 = ranks.get(bkcounter);
			int added = v1+v2;
			if (added < min){
				min = added;
			}
			bkcounter --;
		}
		System.out.println(maxValue);
	}
}
