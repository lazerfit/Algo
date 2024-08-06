import java.util.Stack;
class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        
        Stack<Integer> stack = new Stack<>();
        
        A:for ( int m : moves){
            for ( int i = 0; i < board.length; i++){
                if(board[i][m-1] != 0) {
                    
                    if(stack.isEmpty()){
                        stack.push(board[i][m-1]);
                        board[i][m-1] = 0;
                    } 
                    
                    else if (!stack.isEmpty() && stack.peek().equals(board[i][m-1])){
                        stack.pop();
                        board[i][m-1] = 0;
                        answer += 2;
                    }
                    
                    else if (!stack.peek().equals(board[i][m-1])) {
                        stack.push(board[i][m-1]);
                        board[i][m-1] = 0;
                    }
                    
                    continue A;
                }
            }
        }
        return answer;
    }
}