import java.util.ArrayList;

// Unfinished 

public class HAlien {
	public int feels;
	public int eyes;
	public int testFeels;
	public int differFeels;
	
	public static int max2;
	
	public HAlien(int feels, int eyes){
		this.feels = feels;
		this.eyes = eyes;
	}
	
	public static void rulesSameEyes(HAlien alien1, HAlien alien2){
		if (alien1.eyes == alien2.eyes) {
			alien1.testFeels = alien1.testFeels + 1;
			alien2.testFeels = alien2.testFeels + 1;
		}
	}
	
	public static void rulesDiffer1(HAlien alien1, HAlien alien2){
		if (alien1.eyes + 1 == alien2.eyes) {
			// differ by 1
			alien1.differFeels = alien1.differFeels + 1;
			alien2.differFeels = alien2.differFeels + 1;
		} else if (alien2.eyes + 1 == alien1.eyes) {
			// differ by 1
			alien1.differFeels = alien1.differFeels + 1;
			alien2.differFeels = alien2.differFeels + 1;
		}
	}
	
	public static void permuteStart ( ArrayList<HAlien> aliens) {
        permute(aliens, 0, aliens.size()-1); }

    public static void permute( ArrayList<HAlien> aliens, int low, int high ) {
        if ( low == high ) {
            System.out.println(aliens);
        }
        else {
            HAlien tmp = aliens.get(low);
            for ( int i = low; i <= high; i++ ) {
            	aliens.set(low, aliens.get(i));
            	aliens.set(i, tmp);
                permute( aliens, low+1, high );
                aliens.set(i, aliens.get(low));
            }
            aliens.set(low, tmp); }
    }
    
    public static void check(ArrayList<HAlien> aliens) {
    	ArrayList<HAlien> cpy = new ArrayList<>(aliens);
    	ArrayList<HAlien> cpy2 = new ArrayList<>();

    	int s = cpy.size();
    	for (int i=0; i<s; i++) {
    		for (int j=0; j<cpy.size(); j++){ 
    			rulesSameEyes(cpy.get(0), cpy.get(j));
    			rulesDiffer1(cpy.get(0), cpy.get(j));
    		}
    		cpy2.add(cpy.get(0));
    		cpy.remove(0);
    	}
    }

	
	public static void main(String[] args) {
		int noAliens = 3;
		int[] alienFeels = {1,2,3};
		int[] eyes = {2,3,4};
		
		ArrayList<HAlien> aliens = new ArrayList<>();
		for (int i: alienFeels) {
			HAlien newAlien = new HAlien(i,2);
			aliens.add(newAlien);
		}
		
		//permuteStart(aliens);
		
		for (int k=0; k<noAliens; k++) {
			aliens.get(k).eyes = 3;
		}
		
		
	}

}
