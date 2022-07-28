package CmdLoop;

import java.util.Scanner;

public class CmdLoop {
    public static void main(String[] args) {
        System.out.println("This is worldle help...");
        System.out.print("Command?> ");
        Scanner input = new Scanner(System.in);
        String line = input.nextLine();
        
        while(!line.equalsIgnoreCase("exit") && !line.equalsIgnoreCase("quit")) {
            if (!line.isEmpty()) {
                switch(line) {
                    case "help":
                    case "?":
                        System.out.println("Processing help..");
                        break;
                    case "add":
                        System.out.println("Processing add..");
                        break;
                    case "match":
                        System.out.println("Processing match..");
                        break;
                    case "remove":
                        System.out.println("Processing remove..");
                        break;
                    default:
                        System.out.println("Command unrecognized");
                }
            }

            System.out.print("Command?> ");
            line = input.nextLine();
        }

        input.close();
        System.out.println("Goodbye!");
    }
}