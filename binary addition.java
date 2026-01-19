// User function Template for Java
/*
Given two binary strings s1 and s2 consisting of only 0s and 1s. Find the resultant string after adding the two Binary Strings.
Note: The input strings may contain leading zeros but the output string should not have any leading zeros.

Input: s1 = "1101", s2 = "111"
Output: 10100
Explanation:
 1101
+ 111
10100
Input: s1 = "00100", s2 = "010"
Output: 110
Explanation: 
  100
+  10
  110
*/
class Solution {
    static String trim(String s){
        int first = s.indexOf('1');
        return (first == -1) ? "0" : s.substring(first);
    }
    static  String addbin(String s1, String s2){
        s1 = trim(s1);
        s2 = trim(s2);
        
        int n = s1.length();
        int m = s2.length();
        if(n<m){
            return addbin(s2,s1);
        }
        int j = m - 1;
        int carry = 0;
        StringBuilder result = new StringBuilder();
        for (int i = n-1 ; i>= 0 ; i--){
            int b1 = s1.charAt(i) - '0';
            
            int sum = b1 + carry;
            if (j>=0){
                int b2 = s2.charAt(j) - '0';
                sum += b2;
                j--;
            }
            int bit = sum % 2;
            carry = sum/2;
            result.append((char)(bit + '0'));
        }
        if (carry > 0) result.append('1');
        return result.reverse().toString();
    }
    public String addBinary(String s1, String s2) {
        // code here
        return addbin(s1,s2);
    }
}
