import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;

public class Vowels {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        HashMap<String, Integer> counts = new HashMap<>();
        counts.put("a", 0);
        counts.put("e", 0);
        counts.put("i", 0);
        counts.put("o", 0);
        counts.put("u", 0);
        String a = "a";
        String e = "e";
        String i = "i";
        String o = "o";
        String u = "u";

        while (true){
            //System.out.println(in.hasNext());
            String aLine = in.nextLine();
            //System.out.println(aLine);

            for (int k=0; k<aLine.length();k++){
                String theChar = aLine.substring(k,k+1);
                //System.out.println("THE CHAR BELOW:");
                //System.out.println(theChar);

                if (a.equals(theChar.toLowerCase())) {
                    counts.put("a", counts.get("a")+1);
                } else if (e.equals(theChar.toLowerCase())) {
                    counts.put("e", counts.get("e")+1);
                } else if (i.equals(theChar.toLowerCase())) {
                    counts.put("i", counts.get("i")+1);
                } else if (o.equals(theChar.toLowerCase())) {
                    counts.put("o", counts.get("o")+1);
                } else if (u.equals(theChar.toLowerCase())) {
                    counts.put("u", counts.get("u")+1);
                }

            }

            //System.out.println(counts.get("a"));
            //System.out.println(counts.get("u"));

            //System.out.println("DONE");

            ArrayList<Integer> values = new ArrayList(counts.values());
            ArrayList<Integer> unqValues = new ArrayList();
            ArrayList<String> keys = new ArrayList(counts.keySet());


            Set<Integer> s = new HashSet<Integer>(values);

            Iterator myit = s.iterator();
            while (myit.hasNext()) {
                Integer theV = (int) myit.next();
                unqValues.add(theV);
            }

            String output = "";

            Collections.sort(unqValues);
            //System.out.println("UNQ V");
            //System.out.println(unqValues.size());

            for (int l=0; l<unqValues.size(); l++){

                //System.out.println(unqValues.get(unqValues.size()-l-1));
                // get all keys of same value

                ArrayList<String> theCorVowels = new ArrayList<>();

                for (int w=0; w<keys.size(); w++) {
                    if (values.get(w) == unqValues.get(unqValues.size()-l-1)){
                        theCorVowels.add(keys.get(w));
                    }
                }

                for (int p=0; p<theCorVowels.size(); p++){

                    if (theCorVowels.get(p).equals("a")){
                        output += "a:" + unqValues.get(unqValues.size()-1-l) + " ";
                    }
                }
                for (int p=0; p<theCorVowels.size(); p++){
                    if (theCorVowels.get(p).equals("e")){
                        output += "e:" + unqValues.get(unqValues.size()-1-l) + " ";
                    }
                }
                for (int p=0; p<theCorVowels.size(); p++){
                    if (theCorVowels.get(p).equals("i")){
                        output += "i:" + unqValues.get(unqValues.size()-1-l) + " ";
                    }
                }
                for (int p=0; p<theCorVowels.size(); p++){
                    if (theCorVowels.get(p).equals("o")){
                        output += "o:" + unqValues.get(unqValues.size()-1-l) + " ";
                    }
                }
                for (int p=0; p<theCorVowels.size(); p++){
                    if (theCorVowels.get(p).equals("u")){
                        output += "u:" + unqValues.get(unqValues.size()-1-l) + " ";
                    }
                }



            }


            System.out.println(output);
            break;
        }
    }
}
