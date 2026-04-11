import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        
        int dotInRow = (1 << N) + 1;
        int totalDots = dotInRow * dotInRow;
        
        System.out.println(totalDots);
    }
}