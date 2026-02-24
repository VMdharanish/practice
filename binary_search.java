import java.util.Scanner;
class binary_search{
    public static int binarysearch(int[] arr,int left,int right,int tar){
        if (arr.length == 0){
            return -1;
        }
        int mid = (left + right)/2;

        if(tar == arr[mid]){
            return mid;
        }
        else if(tar < arr[mid]){
            return binarysearch(arr,left,mid-1,tar);
        }else{
            return binarysearch(arr,mid+1,right,tar);
        }
    }
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        System.out.println("Enter the size of the array: ");
        int n = scan.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter sorted array of elements: ");
        for(int i = 0; i < n ; i++){
            arr[i] = scan.nextInt();
        }
        System.out.println("Enter the target element: ");
        int tar = scan.nextInt();
        int result = binarysearch(arr,0,n-1,tar);
        if (result != -1){
            System.out.println("Element found at the index of :" + result);
        }else{
            System.out.println("Element not found");
        }scan.close();5
    }
}