import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int result = 1;
        for (int i = 0; i < 3; i++) {
            result *= Integer.parseInt(br.readLine());
        }

        int[] count = new int[10];
        do {
            count[result % 10]++;
            result /= 10;
        } while (result > 0);

        StringBuilder sb = new StringBuilder(30);

        for (int n : count) {
            sb.append(n).append("\n");
        }
        System.out.println(sb);

//
//        int[] count = new int[10];
//        String sen = Integer.toString(result);
//
//        for (char c : sen.toCharArray()) {
//            int num = c - '0';
//            count[num]++;
//        }
//
//        for (int n : count) {
//            bw.write(Integer.toString(n));
//            bw.newLine();
//        }
//        bw.flush();
    }
}