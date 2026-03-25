import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int time = 0;

        for (int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            
            if (c < 'D') time += 3;
            else if (c < 'G') time += 4;
            else if (c < 'J') time += 5;
            else if (c < 'M') time += 6;
            else if (c < 'P') time += 7;
            else if (c < 'T') time += 8;
            else if (c < 'W') time += 9;
            else time += 10;
        }
        
        System.out.println(time);
    }
}