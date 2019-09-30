import java.math.BigInteger;
import java.math.BigInteger.*;

public class Problem16 {

    public static int sumOfDigits(BigInteger x) {
        int sum = 0;
        String string = x.toString();
        for (int i = 0; i < string.length(); i++) {
            sum += Integer.parseInt(string.substring(i, i+1));
        }

        return sum;
    }
    public static void main (String[] args) {
        BigInteger n = BigInteger.valueOf(2);
        n = n.pow(1000);
        System.out.println(n);
        System.out.println(sumOfDigits(n));

    }
}

