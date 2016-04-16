import java.util.Scanner;

public class Footballers {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		String input = in.nextLine();
		//System.out.println(name);
		String[] parts = input.split(" ");
		String name = parts[0];
		Integer age = Integer.parseInt(parts[1]);
		Integer weight = Integer.parseInt(parts[2]);
		
		if (age>17){
			System.out.println(name +  " Senior");
		} else if (weight >= 80) {
			System.out.println(name +  " Senior");
		} else {
			System.out.println(name +  " Junior");
		}
		
	}

}
