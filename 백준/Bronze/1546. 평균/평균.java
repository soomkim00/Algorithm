import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        List<Double> numbers = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            numbers.add(Double.parseDouble(st.nextToken()));
        }

        Double max_value = Collections.max(numbers);

        for (int i = 0; i < N; i++) {
            Double new_num = (numbers.get(i) / max_value * 100);
            numbers.set(i, new_num);
        }

        Double total = 0.0;
        for (int i = 0; i < N; i++) {
            total += numbers.get(i);
        }

        System.out.println(total / N);
    }
}