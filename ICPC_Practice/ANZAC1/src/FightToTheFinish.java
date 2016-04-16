import java.util.Scanner;

public class FightToTheFinish {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n =  sc.nextInt();
		int h = sc.nextInt();
		int r = sc.nextInt();
		
		int[] aF = new int[n];
		float[][] best = new float[n-1][n];
		int minDmg = h;
		int maxDmg = h+r;
		
		for (int i=0;i<n;i++){
			aF[i] = sc.nextInt();
		}
		
		for (int i=0;i<n-1;i++){
			int iF = aF[i];
			for (int j = i+1;j<n;j++){
				int jF = aF[j];
				int match = 0;
				int count = 0;
				for (int k=1;k<=iF;k++){
					for (int l=1;l<=jF;l++){
						if ((k+l <= maxDmg) && (k+l >= minDmg)){
							match++;
						}
						count++;
					}
				best[i][j] = (float)match/count;
				}
			}
		}
		
		float max = 0.0f;
		int bestI = 0;
		int bestJ = 0;
			
		for (int i=0;i<n-1;i++){
			for (int j=i+1;j<n;j++){
				if (best[i][j] > max){
					max = best[i][j];
					bestI = i;
					bestJ = j;
				}
			}
		}
		
		if (max == 0){
			System.out.println("WELL WE TRIED");
		}
		else {
			System.out.println("d" + aF[bestI] + " d" + aF[bestJ]);
		}
		
		sc.close();
	}

}
