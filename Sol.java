/*1784. Check if Binary String Has at Most One Segment of Ones
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a binary string s ​​​​​withou
  */
class Sol {
    public boolean checkOnesSegment(String s) {
       return !s.contains("01");
    }
}
