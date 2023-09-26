import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int idx = 0; idx < t; idx++) {
            int r = sc.nextInt();
            String s = sc.nextLine();

            for (int i = 1; i < s.length(); i++) {
                for (int j = 0; j < r; j++) System.out.print(s.charAt(i));
            }
            System.out.println();
        }
    }
}