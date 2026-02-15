public class byte_short {
    void byte_(){
        byte a = 127;
        a += 65;
        System.out.println(a);
    }void b(){
        byte b = 127;
        b++;
        System.out.println(b);
    }
    public static void main(String[] args) {
        byte_short a = new byte_short();
        a.byte_();
        a.b();
    }
}