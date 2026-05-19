

public class specifi_insertion {
    //to insert an element at a specific position in an array by shifting the elements to the right and then
    //  inserting the new element at the desired positioN.
    public static void main(String[] args){
        int a[] = new int[]{1,2,3,4,5,6,8,9,10};
        int element = 7;
        int positiion = 6;
        for(int i = a.length -1;i >=positiion;i--){
            a[i] = a[i - 1];
        }
        a[positiion] = element;
        for(int i = a.length -1;i >=0;i--){
            System.err.println(a[i]);
        }
    }
}
