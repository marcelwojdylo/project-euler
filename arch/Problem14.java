import java.util.ArrayList;

public class Problem14 {
    public static int getCollatzSize(Long n) {
        ArrayList<Long> collatz = new ArrayList<Long>();
        Long number = n;
        while (number != 1) {
            // System.out.println(number);
            collatz.add(number);
            if (number % 2 == 0) {
                number = number/2;
            } else {
                number = 3*number+1;
            }
        }
        collatz.add(1L);
        return collatz.size();
    }
    public static void main (String[] args) {
        // int size = getCollatzSize(1000000L);
        // System.out.println(size);

        int longestCollatzSize = 0;
        for (Long i = 1L; i <1000000; i++) {
            int size = getCollatzSize(i);
            // System.out.println("Checking size of Collatz sequence for i = "+i+"\nThe size is : "+size);
            if (size>longestCollatzSize) {
                System.out.println("Largest collatz sequence so far is for n = "+i);
                longestCollatzSize = size;
            }
        }
        System.out.println(longestCollatzSize);

    }
}

// The following iterative sequence is defined for the 
// set of positive integers:

// n → n/2 (n is even)
// n → 3n + 1 (n is odd)