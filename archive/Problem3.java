import java.util.ArrayList;
import java.util.Collections;
import java.text.ParseException;
import java.util.concurrent.TimeUnit;
import java.time.Instant;
import java.time.Duration;

// The largest prime factor of 600851475143 is 6857
// Finding the LPF took: 11108 ms
// To the best of our knowledge the LPF is: 6857
// Finding the LPF took: 47 ms

public class Problem3 {

    private static long TARGET = 600851475143L;
    private static long CASE = TARGET;

    // private static long largestPrimeFactor(long l) {
    //     return Collections.max(getPrimeFactors(l));
    // }

    // private static ArrayList<Long> getPrimeFactors (long number) {

    //     ArrayList<Long> result = new ArrayList<Long>();
    //     ArrayList<Long> primeNumbersInRange = getPrimesUnder(number);

    //     long currentValue = number;
    //     long nextPrimeIndex = 0;

    //     while (!isPrime(currentValue)) {
    //         System.out.println ("Extracting prime factors of: "+currentValue);
    //         long currentPrime = (long) primeNumbersInRange.get((int) nextPrimeIndex);
    //         if (currentValue % currentPrime == 0) {
    //             System.out.println("Current value of "+currentValue+" is divisible by "+currentPrime);
    //             currentValue /= currentPrime;
    //             result.add(currentPrime);    
    //         } else {
    //             nextPrimeIndex++;
    //             System.out.println(currentValue+" is not divisible by " +currentPrime+ ", next prime:" + primeNumbersInRange.get((int) nextPrimeIndex));
    //         }
    //     }
    //     result.add(currentValue);
    //     System.out.println("The largest prime factor of " + number + " is "+currentValue);

    //     return result;
    // }



    // private static ArrayList<Long> getPrimesUnder(long limit) {
    //     System.out.println("Getting primes under "+limit);
    //     ArrayList<Long> results = new ArrayList<Long>();
    //     for (long i = 2; i <= Math.sqrt(limit); i ++) {
    //         if (isPrime(i)) {
    //             results.add(i);
    //             System.out.println("   Found "+results.size()+" primes so far.");
    //         }
    //     }
    //     System.out.println("   Found "+results.size()+" primes so far. These are:");
    //     for (Object o : results) {
    //         System.out.println(o);
    //     }
    //     System.out.println("   Found a total of "+results.size()+" primes.");

    //     return results;
    // }

    // private static boolean isPrime(long l) {
    //     System.out.println("      Checking if " + l +" is prime.");
    //     for (long i = 2; i <= Math.sqrt(l); i++) {
    //         if (l % i == 0) {
    //             return false;
    //         }
    //     }
    //     System.out.println("      "+l+" is prime!!!!!!!!!!!!!!!!!!!!!!!!!!");
    //     return true;
    // }
    public static void main (String[] args) {
        Instant start = Instant.now();
        // largestPrimeFactor(CASE);
        long value = 600851475143L;
        long prime = 2;
        while (value >= prime) {
            if (value % prime == 0) {
                value /= prime;
            } else {
                prime++;
            }
        }
        System.out.println("To the best of our knowledge the LPF is: "+prime);
        Instant finish = Instant.now();
        long timeElapsed = Duration.between(start, finish).toMillis();  //in millis
        System.out.println("Finding the LPF took: "+timeElapsed+" ms");
    }
}