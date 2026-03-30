import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        
        String[] croatianAlphabets = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        
        for (String alphabet : croatianAlphabets) {
            if (input.contains(alphabet)) {
                input = input.replace(alphabet, "*");
            }
        }
        
        System.out.println(input.length());
    }
}