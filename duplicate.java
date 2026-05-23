import java.util.*;

class dup {
    public static void main(String[] args) {
        int[] arr = new int[]{1, 2, 3, 4, 2, 5, 5, 6, 7, 6, 9};
        for (int i = 0; i < arr.length; i++) {
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[i] == arr[j]) {
                    System.out.println("Duplicate numbers : " + arr[j]);
                }
            }
        }
    }
}
