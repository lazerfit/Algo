import java.util.Stack;
class Solution
{
    public int solution(String s)
    {
        int n = s.length();
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < n; i++){
            char ch = s.charAt(i);
            if(stack.isEmpty() || !stack.peek().equals(ch)) {
                stack.push(ch);
            } else {
                stack.pop();
            }
        }
        

        return stack.isEmpty() ? 1 : 0;
    }
}