public class Problem7 {

    private static boolean isPrime(long l) {
        // System.out.println("      Checking if " + l +" is prime.");
        for (long i = 2; i <= Math.sqrt(l); i++) {
            if (l % i == 0) {
                return false;
            }
        }
        // System.out.println("      "+l+" is prime!!!!!!!!!!!!!!!!!!!!!!!!!!");
        return true;
    }
    public static void main (String[] args) {
        boolean found = false;
        int number = 2;
        int primesFound = 0;
        while (!found) {
            if (isPrime(number)) {
                primesFound++;
                if(primesFound == 10001) {
                    System.out.println("The 10,001st prime is "+number);
                    found = true;
                }
                System.out.println("Found primes: "+primesFound);
            }
            number++;
        }   
    }
}