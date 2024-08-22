import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;

public class Main {
    static ArrayDeque<Integer> stack = new ArrayDeque<>();
    static int answer = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            solution(Integer.parseInt(br.readLine()));
        }

        for (int num : stack) {
            answer += num;
        }

        System.out.println(answer);
    }

    private static void solution(int n) {
        if (n != 0) {
            stack.addLast(n);
        } else {
            stack.removeLast();
        }
    }
    
}