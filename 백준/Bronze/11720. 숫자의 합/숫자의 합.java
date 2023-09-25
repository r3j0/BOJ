import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        sc.nextLine();
        String s = sc.nextLine();
        
        int sum_value = 0;
        for (int i = 0; i < n; i++) sum_value += (int)s.charAt(i) - '0';
        
        System.out.println(sum_value);
    }
}