public class Problem10 {

    public static final long TARGET = 2_000_000L;
    public static void main (String[] args) {
        long sum = 0;
        for (long i = 2; i < TARGET; i++) {
            if (isPrime(i)) {
                sum += i;
                System.out.println("Adding "+i);
            }
        }
        System.out.println(sum);
    }

    public static boolean isPrime(long n) {
        for (long i = 2; i <= Math.sqrt(n); i++) {
            if (n%i==0) return false;
        }
        return true;
    }

}