import java.util.ArrayList;

public class Main {

    public static ArrayList<Integer> printDivisors(int n) {
        ArrayList<Integer> divisors = new ArrayList<>();
        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                if (n / i == i) {
                    divisors.add(i);
                }
                else {
                    divisors.add(i);
                    divisors.add(n / i);
                }
            }
        }
        return divisors;
    }

    public static void main(String[] args) {
        ArrayList<Integer> divisors = printDivisors(10);
        for (int divs : divisors) {
            System.out.print(divs + " ");
        }
    }
}
