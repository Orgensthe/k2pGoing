import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the isBalanced function below.
    static String isBalanced(String s) {
        String result = "YES";
        Stack<Character> sStack = new Stack<>();

        for (char bracket : s.toCharArray()) {
            if (bracket == ')' || bracket == '}' || bracket == ']') {
                if (!sStack.isEmpty()) {
                    int subResult = bracket - sStack.pop();
                    if (subResult != 1  && subResult != 2) {
                        sStack.clear();
                        result = "NO";
                        break;
                    }
                } else {
                    result = "NO";
                    break;
                }
            } else {
                sStack.push(bracket);
            }
        }

        if(!sStack.isEmpty())
            result = "NO";

        return result;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int t = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int tItr = 0; tItr < t; tItr++) {
            String s = scanner.nextLine();

            String result = isBalanced(s);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}
