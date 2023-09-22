import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum_value = 0;
        int max_value = 0;
        
        int tmp;
        for (int i = 0; i < n; i++) {
            tmp = sc.nextInt();
            
            sum_value += tmp;
            if (max_value < tmp) max_value = tmp;
        }

        System.out.println((double)sum_value / max_value * 100 / n);
    }
}