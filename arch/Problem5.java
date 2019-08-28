// My best guess is: 232792561
// This took 20301555 milliseconds

import java.time.Instant;
import java.time.Duration;

public class Problem5 {

    public static void main (String[] args) {

        boolean found = false;
        int number = 1;
        Instant start = Instant.now();
        int[] divisors = {2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
        System.out.println();
        System.out.print("Checking number: ");
        while(!found) {
            String str = Integer.toString(number);
            for (int i = 0; i < str.length(); i++) {
                System.out.print("\b");
            }
            System.out.print(number);
            for (int d : divisors) {
                if (number % d != 0) {
                    break;
                }
                if(d==20) {
                    found = true;
                    System.out.println("My best guess is: "+number);
                }
            }
            number++;
        }


        // while (!found) {
        //     System.out.println("Checking number: "+number);
        //     if (
        //         number % 2 == 0 &&
        //         number % 3 == 0 &&
        //         number % 4 == 0 &&
        //         number % 5 == 0 &&
        //         number % 6 == 0 &&
        //         number % 7 == 0 &&
        //         number % 8 == 0 &&
        //         number % 9 == 0 &&
        //         number % 10 == 0 &&
        //         number % 11 == 0 &&
        //         number % 12 == 0 &&
        //         number % 13 == 0 &&
        //         number % 14 == 0 &&
        //         number % 15 == 0 &&
        //         number % 16 == 0 &&
        //         number % 17 == 0 &&
        //         number % 18 == 0 &&
        //         number % 19 == 0 &&
        //         number % 20 == 0
        //     ) {
        //         found = true;
        //         System.out.println("The answer is: "+number);
        //     }
        //     number++;
        // }
        Instant finish = Instant.now();
        long timeElapsed = Duration.between(start, finish).toMillis();
        System.out.println("This took "+timeElapsed+" milliseconds");
    }
}