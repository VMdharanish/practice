import java.util.Scanner;

class ARP_RARP_Simulation {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Select Protocol (ARP/RARP): ");
        String protocol = sc.nextLine();

        if (protocol.equalsIgnoreCase("ARP")) {

            System.out.print("Enter IP Address: ");
            String ip = sc.nextLine();

            System.out.println("MAC Address for IP " + ip + " is: AA:BB:CC:DD:EE:FF");

        } 
        else if (protocol.equalsIgnoreCase("RARP")) {

            System.out.print("Enter MAC Address: ");
            String mac = sc.nextLine();
 
            System.out.println("IP Address for MAC " + mac + " is: 192.168.1.10");

        } 
        else {

            System.out.println("Invalid Protocol Selected");

        }

        sc.close();
    }
}
