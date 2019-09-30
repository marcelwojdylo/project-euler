import java.util.ArrayList;
import java.util.Collections;

public class Problem4 {

    static ArrayList<Integer> range() {
        ArrayList<Integer> range = new ArrayList<Integer>();
        for (int i = 100; i <= 999; i++) {
            range.add(i);
        }
        return range;
    };

    static boolean isPalindrome(int input) {
        String str = Integer.toString(input);
        if (str.equals(reverseString(str))) {
            return true;
        }
        return false;
    }

    static String reverseString(String string) {
        String result = "";
        for (int i = string.length() - 1; i>=0; i--) {
            result += string.charAt(i);
        }
        return result;
    }

    static String answer () {
        ArrayList<Integer> range = range();
        ArrayList<Integer> results = new ArrayList<Integer>();
        for (int i = range.size() - 1; i >= 0; i--) {
            int x = range.get(i);
            for (int j = i; j >= 0; j--) {
                System.out.println(i+" "+j);
                int y = range.get(j);
                if (isPalindrome(x*y)) {
                    results.add(x*y);
                    System.out.println("Palindrome found: "+x*y + "x = "+x+", y = "+y);
                }
            }
        }
        return "The answer is: "+ Collections.max(results);
    }
    public static void main (String[] args) {
        System.out.println(answer());

    }
}