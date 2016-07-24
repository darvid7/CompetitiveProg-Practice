import java.util.Scanner;
// correct :D 
public class Arithmetic {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		Integer a = in.nextInt();
		Integer b = in.nextInt();
		Long aNew = new Long(a);
		Long bNew = new Long(b);

		System.out.println((aNew+bNew) + "  " + (aNew-bNew));
	}

}
