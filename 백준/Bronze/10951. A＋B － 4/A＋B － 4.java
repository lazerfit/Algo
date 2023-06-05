import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
 
public class Main {
	public static void main(String args[]) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str;
        
        while((str=br.readLine())!=null){
            int a = str.charAt(0) - 48;
			int b = str.charAt(2) - 48;
            
            System.out.println(a+b);
        }
    }
}