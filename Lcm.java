/*lcm of two numbers*/

class solution{
  public int lcm(int a,int b){
    int c = Math.max(a,b);
    int d = Math.min(a,b);
    for(int i = d,i<=a*b;i+=d){
      if(i%c==0){
        return i;
      }
    return a*b;
  }
