import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        while(T-- > 0) {
            String p = br.readLine();
            int n = Integer.parseInt(br.readLine());
            String arrStr = br.readLine();
            Deque<Integer> dq = new ArrayDeque<>();
            String[] nums = arrStr.substring(1, arrStr.length() - 1).split(",");
            for(int i = 0; i < n; i++) {
                if(!nums[i].isEmpty()) dq.add(Integer.parseInt(nums[i]));
            }
            boolean rev = false, err = false;
            for(char c : p.toCharArray()) {
                if(c == 'R') rev = !rev;
                else {
                    if(dq.isEmpty()) { err = true; break; }
                    if(rev) dq.pollLast();
                    else dq.pollFirst();
                }
            }
            if(err) sb.append("error\n");
            else {
                sb.append("[");
                while(!dq.isEmpty()) {
                    sb.append(rev ? dq.pollLast() : dq.pollFirst());
                    if(!dq.isEmpty()) sb.append(",");
                }
                sb.append("]\n");
            }
        }
        System.out.print(sb);
    }
}