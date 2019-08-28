public class Problem6 {

    private static int sumOfSquares(int n) {
        int result = 0;
        for (int i = 1; i <=n; i++) {
            result += i*i;
        }
        return result;
    }

    private static int squareOfSums(int n) {
        int result = 0;
        for (int i = 1; i<=n; i++) {
            result += i;
        }
        return result*result;
    }

    public static void main (String[] args) {
        System.out.println("The sum of squares is: ");
        System.out.println(sumOfSquares(100));
        System.out.println("The sqare of sums is: ");
        System.out.println(squareOfSums(100));
        System.out.println("The difference is: ");
        System.out.println(squareOfSums(100)-sumOfSquares(100));
    }
}