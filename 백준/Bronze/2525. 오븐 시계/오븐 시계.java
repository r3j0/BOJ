import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int result = a * 60 + b + c;
        if (result >= 1440) result -= 1440;

        System.out.println((result / 60) + " " + (result % 60));
    }
}