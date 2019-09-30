import java.util.ArrayList;

public class Problem2 {

    private static int sumOfEvenFibonacci(int limit) {
        return sumOfEvens(fibonaccis(limit));
    }

    private static int sumOfEvens(ArrayList list) {
        int sum = 0;

        for (int i = 0; i < list.size(); i++) {
            int element = (int) list.get(i);
            if (element % 2 == 0) {
                sum += element;
            }
        }

        return sum;
    }

    private static ArrayList fibonaccis(int limit) {
        ArrayList <Integer> fibs = new ArrayList<Integer>();
        int current = 1;
        int next = 2;
        fibs.add(current);
        fibs.add(next);
        while (next<=limit) {
            int temp = next;
            next += current;
            current = temp;
            fibs.add(next);
            System.out.println(next);
        }
        return fibs;

    }
    public static void main (String[] args) {
        System.out.println(sumOfEvenFibonacci(4000000));
    }
}