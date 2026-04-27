import java.io.*;
import java.util.*;

public class Main {
    static int N, M, max = 0;
    static int[][] board;
    static boolean[][] vis;
    static int[] dy = {-1, 1, 0, 0}, dx = {0, 0, -1, 1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        vis = new boolean[N][M];
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) board[i][j] = Integer.parseInt(st.nextToken());
        }
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                vis[i][j] = true;
                dfs(i, j, 1, board[i][j]);
                vis[i][j] = false;
                checkT(i, j);
            }
        }
        System.out.println(max);
    }

    static void dfs(int y, int x, int depth, int sum) {
        if(depth == 4) {
            max = Math.max(max, sum);
            return;
        }
        for(int i = 0; i < 4; i++) {
            int ny = y + dy[i], nx = x + dx[i];
            if(ny >= 0 && ny < N && nx >= 0 && nx < M && !vis[ny][nx]) {
                vis[ny][nx] = true;
                dfs(ny, nx, depth + 1, sum + board[ny][nx]);
                vis[ny][nx] = false;
            }
        }
    }

    static void checkT(int y, int x) {
        for(int i = 0; i < 4; i++) {
            int sum = board[y][x];
            boolean possible = true;
            for(int j = 0; j < 3; j++) {
                int dir = (i + j) % 4;
                int ny = y + dy[dir], nx = x + dx[dir];
                if(ny < 0 || ny >= N || nx < 0 || nx >= M) {
                    possible = false; 
                    break;
                }
                sum += board[ny][nx];
            }
            if(possible) max = Math.max(max, sum);
        }
    }
}