public class array {
    public static void main(String[] args) {
        int a[] = {2,4,5,3,8,7,9,14,11};
        int e = 0;
        for(int b:a){
            if (b%2 == 0)
                e += 1;
        }
        int o = a.length - e;
        System.out.println("Even numbers: " + e);
        System.out.println("Odd numbers: " + o);
    }
}
