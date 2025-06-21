import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();

        String[] tokens = line.split("\\s+");

        int total = 0;

        for (int i = 0; i < tokens.length; i++) {
            int num = Integer.parseInt(tokens[i]);
            total += num * num;
        }

        int result = total % 10;
        System.out.println(result);


    }
}