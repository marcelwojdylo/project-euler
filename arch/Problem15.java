import java.math.BigInteger;

public class Problem15 {

    // public static long makeFactorial(long n) {
    //     long factorial = 1;
    //     for (long i = 1; i <=n; i++) {
    //         factorial *= i;
    //     }
    //     return factorial;
    // }

    public static BigInteger combinationFormula(long n, long r) {
        BigInteger result;

        return makeFactorial(n).divide(makeFactorial(r).multiply(makeFactorial(n-r)));
    }

    public static BigInteger makeFactorial (long n) {
        BigInteger factorial = BigInteger.valueOf(1);
        for (long i = 1; i<=n; i++) {
            factorial = factorial.multiply(BigInteger.valueOf(i));
        }
        return factorial;
    }
    public static void main (String[] args) {
        System.out.println(combinationFormula(40, 20));
    }

}