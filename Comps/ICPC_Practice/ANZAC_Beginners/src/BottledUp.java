import java.util.Scanner;

public class BottledUp {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int totalVolume = in.nextInt();
		int b1Volume = in.nextInt();
		int b2Volume = in.nextInt();
		
		int curValue = totalVolume;
		int rem;
		boolean found = false;
		
		while (!found) {
			rem = curValue % b1Volume;
			if (rem != 0) {
				//System.out.println(curValue);

				if (totalVolume-curValue % b2Volume == 0) {
					found = true;
					System.out.println(totalVolume/b1Volume + " " + rem/b2Volume);
					break;
				}
				curValue = curValue - b2Volume;
				if (curValue < b1Volume) {
					found = false;
					System.out.println("Impossible");
					break;
				}
			} else {
				//System.out.println("else" + curValue);

				// rem == 0 
				int noB1 = curValue / b1Volume;
				int needToFill = totalVolume - curValue;
				if (needToFill % b2Volume == 0) {
					found = true;
					System.out.println(noB1 + " " + needToFill/b2Volume);
					break;
				} else {
					found = false;
					System.out.println("Impossible");
					break;
				}
			}
		}
		
	}
}
