public class Problem1 {
    private static int sumOfMultiples3and5(int limit) {
        int sum = 0;
        for (int i = 0; i<limit; i++) {
            if (i%3 == 0 || i%5 == 0) {
                sum += i;
            }
        }
        return sum;
    }
    public static void main (String[] args) {
        System.out.println(sumOfMultiples3and5(1000));
    }

}