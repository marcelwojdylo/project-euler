import java.util.ArrayList;


// 200
// 375
// 425
// Sum: 1000
// Is this triple pythagorean? true
// FOUND IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!

public class Problem9 {

    public static void main (String[] args) {
        for (long i = 0; i <= 1000; i++) {
            if (i % 2 == 0) makeDickson(i);
        }
    }

    private static boolean isTriplePythagorean (long[] triple) {
        return (triple[0]*triple[0]+triple[1]*triple[1]==triple[2]*triple[2]);
    }
    private static boolean isTriplePythagorean (Long[] triple) {
        return (triple[0]*triple[0]+triple[1]*triple[1]==triple[2]*triple[2]);
    }

    public static boolean areCoprime(long a, long b) {
        long higher = (a > b) ? a : b;
        for (long i = 2; i <= higher; i++) {
            if (a % i == 0 && b % i == 0) return false;
        }
        return true;
    }

    private static boolean isSquare(long k) {
        if (Math.sqrt(k)-Math.ceil(Math.sqrt(k))==0) {
            return true;
        }
        return false;
    }

    public static boolean isSumEqual(long targetSum, long[] triple) {
        long sum = 0;
        for (long l : triple) {
            sum += l;
        }
        if (sum == targetSum) return true;
        return false;
    }

    public static boolean isSumEqual(long targetSum, Long[] triple) {
        long sum = 0;
        for (Long l : triple) {
            sum += l;
        }
        if (sum == targetSum) return true;
        return false;
    }

    public static void printArray(long[] array) {
        for (long l : array) System.out.println(l);
    }
    public static void printArray(Long[] array) {
        for (Long l : array) System.out.println(l);
    }

    public static void printSum(long[] array) {
        long result = 0;
        for (long l : array) result += l;
        System.out.println("Sum: "+result);
    } 

    public static void printSum(Long[] array) {
        long result = 0;
        for (long l : array) result += l;
        System.out.println("Sum: "+result);
    } 


// DICKSON

    // public static void checkWithDickson

    public static ArrayList<Long[]> makeDickson (long r) {
        ArrayList<Long[]> factorPairs = findFactorPairs((r*r)/2);
        ArrayList<Long[]> result = new ArrayList<Long[]>();
        for (long i = 0; i < factorPairs.size(); i++) {
            long s = factorPairs.get((int) i)[0];
            long t = factorPairs.get((int) i)[1];
            long a = r + s;
            long b = r + t;
            long c = r + s + t;
            Long[] triple = {a,b,c};
            printArray(triple);
            printSum(triple);
            System.out.println("Is this triple pythagorean? "+isTriplePythagorean(triple));
            if (isSumEqual(1000, triple)) System.out.println("FOUND IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
            result.add(triple);
        }
        return result;
    }

    public static ArrayList<Long[]> findFactorPairs(long product) {
        ArrayList<Long[]> result = new ArrayList<Long[]>();
        for (long i = 1; i <= Math.sqrt(product); i++) {
            for (long j = 1; j <= product; j++) {
                if (i*j == product) {
                    // System.out.println("Found pair of "+i+" and "+j);
                    Long[] pair = {i,j};
                    result.add(pair);
                }
            }
        }
        
        return result;
    }



//PLATO

public static void checkWithPlato() {
    boolean finished = false;
    long n = 0;
    while (!finished) {
        n+=2;
        printSum(makePlato(n));
        System.out.println("Is this triple pythagorean? "+isTriplePythagorean(makePlato(n)));            
        if (isSumEqual(1000, makePlato(n))) {
            finished = true;
            System.out.println("Found!");
        }

        if (n > 60) finished = true;
    }
}

public static long[] makePlato(long n) {
    long a = n;
    long b = (n/2)*(n/2) - 1;
    long c = (n/2)*(n/2) + 1;
    return new long[] {a,b,c};
}

// EUCLID

    private static void checkWithEuclid() {
        for (long k = 1; k<=20; k++) {
            for (long m = 1; m <= 20; m+=2) {
                for (long n = 1; n<=20; n+=2) {
                    if (areCoprime(m, n) && m%2!=0 && n%2!=0) {
                        // printArray(makeEuclid(m, n,k));
                        printSum(makeEuclid(m,n,k));
                        System.out.println("Is this triple pythagorean? "+isTriplePythagorean(makeEuclid(m,n,k)));            
                        if (isSumEqual(1000, makeEuclid(m, n,k))) {
                            System.out.println("Found!");
                        }
                    }
                }
            }
        }

    }

    private static long[] makeEuclid(long m, long n, long k) {
        long a = k*(m*m - n*n);
        long b = k*(2*m*n);
        long c = k*(m*m + n*n);
        return new long[] {a,b,c};
    }

// PYTHAGORAS

    private static void checkWithPythagoras() {
        boolean found = false;
        long n = -1;
        while (!found) {
            n+=2;
            printArray(makePythagoras(n));
            printSum(makePythagoras(n));
            System.out.println("Is this triple pythagorean? "+isTriplePythagorean(makePythagoras(n)));
            if (isSumEqual(1000, makePythagoras(n))) {
                found = true;
                printArray(makePythagoras(n));
            }
            if (n>200) found = true;
        }
    }

    private static long[] makePythagoras(long l) {
        long a = l;
        long b = (a*a-1)/2;
        long c = b+1;
        return new long[] {a,b,c};
    }

// STIEFEL + OZANAM

    public static void checkWithStifelAndOzanam(){
        boolean found = false;
        long n = 0;
        while (!found ) {
            n++;
            if (isSumEqual(1000, makeStifel(n)) || isSumEqual(1000, makeOzanam(n))) {
                found = true;
                System.out.println("Found");
            }
            if (n > 100) found = true;
        }
    }

// STIFEL METHOD

    public static long[] makeStifel(long n) {
        long a = 2*n+1;
        long b = n*a+n;
        long c = b+1;
        long[] triple = {a,b,c};
        for (long l : triple) System.out.println(l);
        long sum = a+b+c;
        System.out.println("Sum: "+sum);
        return triple;
    }

// OZANAM METHOD 

    public static long[] makeOzanam(long n) {
        long a = 4*n+4;
        long b = n*a+(4*n+3);
        long c = b+2;
        long[] triple = {a,b,c};
        for (long l : triple) System.out.println(l);
        long sum = a+b+c;
        System.out.println("Sum: "+sum);
        return triple;
    }

// FIBONACCI METHOD
    private static long kFromN(long n) {
        return 2*n-1;
    }

    private static long nFromK(long k) {
        return (k+1)/2;
    }

    private static long[] generateTripleWithFib(long k) {
        long aSquared = k;

        long elementNumber = nFromK(k);

        long bSquared = 0;
        for (long n = 1; n<elementNumber; n++) {
            bSquared+=kFromN(n);
        }

        long cSquared = 0;
        for (long n = 1; n<=elementNumber; n++) {
            cSquared+=kFromN(n);
        }

        long a = (long) Math.sqrt(aSquared);
        long b = (long) Math.sqrt(bSquared);
        long c = (long) Math.sqrt(cSquared);
        long[] pythagoreanTriple = {a,b,c};
        System.out.println(a+","+b+","+c);
        // System.out.println(a*b*c);
        return pythagoreanTriple;
    }

    private static void lookForAnswerWithFib(long targetSum) {
        boolean found = false;
        long k = -1;
        while (!found) {
            k+=2;
            if (isSquare(k)) {
                System.out.println(k+" is square; checking.");
                long[] triple = generateTripleWithFib(k);
                System.out.print("Is the trip pythagorean? "+isTriplePythagorean(triple));
                long sum = 0;
                for (long i : triple) {
                    sum += i;
                }
                System.out.println("\nSum: "+sum);
                if (sum == targetSum) {
                    found = true;
                    generateTripleWithFib(k);
                } else if (sum > targetSum) {
                    System.out.println("Aborted.");
                    found = true;
                }
            }
        }
        long[] asdasd = {2,4,14};
        System.out.print("Is the trip pythagorean? "+isTriplePythagorean(asdasd));
    }

}



// A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

// a2 + b2 = c2
// For example, 32 + 42 = 9 + 16 = 25 = 52.

// There exists exactly one Pythagorean triplet for which a + b + c = 1000.
// Find the product abc.