class Student {

    String name;         
    static String college = "ABC College"; 
    Student(String name) {
        this.name = name;
    }

    void display() {
        System.out.println("Name: " + name);
        System.out.println("College: " + college);
        System.out.println();
    }
}

public class TestStatic {
    public static void main(String[] args) {

        Student s1 = new Student("Arun");
        Student s2 = new Student("Bala");

        s1.display();
        s2.display();
        Student.college = "XYZ College";

        System.out.println("After changing college:\n");

        s1.display();
        s2.display();
    }
}
