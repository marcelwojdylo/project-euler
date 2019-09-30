public class Problem12 {

    public static long countDivisors(long n) {
        long numberOfDivisors = 0;
        for (long i = 1; i <= Math.sqrt(n); i++) {
            if (n%i==0) numberOfDivisors++;
        }
        System.out.println("The number "+n+" has "+2*numberOfDivisors+" divisors");
        return numberOfDivisors*2;
    }

    public static long makeEnthTriangular(long n) {
        return (n*(n+1))/2;
    }
    public static void main (String[] args) {

        countDivisors(28);

        // boolean found = false;
        // long n = 1;
        // while (!found) {
        //     System.out.println(n);
        //     if(countDivisors(makeEnthTriangular(n)) >= 500) {
        //         found = true;
        //     }
        //     n++;
        // }

    }
}