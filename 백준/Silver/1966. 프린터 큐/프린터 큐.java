import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Collections;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            // 1. 문서의 정보(인덱스, 중요도)를 담을 큐 (int[] 사용)
            ArrayDeque<int[]> queue = new ArrayDeque<>();
            
            // 2. 중요도만 따로 관리하는 우선순위 큐 (내림차순 정렬)
            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

            StringTokenizer st2 = new StringTokenizer(br.readLine());
            for (int idx = 0; idx < n; idx++) {
                int score = Integer.parseInt(st2.nextToken());
                
                queue.add(new int[] {idx, score});
                pq.add(score); // 중요도만 따로 저장
            }

            int order = 1;
            while (!queue.isEmpty()) {
                int[] front = queue.poll(); // 현재 문서를 꺼냄

                // pq.peek()는 현재 남아있는 문서 중 가장 높은 중요도
                if (front[1] == pq.peek()) {
                    // 인쇄 가능한 경우 (현재 문서 중요도 == 최고 중요도)
                    pq.poll(); // 중요도 큐에서도 제거 (인쇄 처리)
                    
                    if (front[0] == m) { // 찾던 문서라면
                        sb.append(order).append('\n');
                        break;
                    }
                    order++; // 다음 순서 준비
                    
                } else {
                    // 중요도가 낮아서 인쇄 불가능하면 뒤로 보냄
                    queue.add(front);
                }
            }
        }
        System.out.print(sb);
    }
}