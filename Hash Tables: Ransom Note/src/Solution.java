import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the checkMagazine function below.
    static void checkMagazine(String[] magazine, String[] note) {
        Map<String, Integer> magazineMap = new HashMap<>();
        Boolean result = true;

        for (String word : magazine) {
            if (!magazineMap.containsKey(word)) {
                magazineMap.put(word, 1);
            } else {
                Integer wordNum = magazineMap.get(word);
                magazineMap.remove(word);
                magazineMap.put(word, wordNum + 1);
            }
        }

        for (String word : note) {
            if (magazineMap.containsKey(word)) {
                Integer num = magazineMap.get(word);
                if (num == 0) {
                    result = false;
                    System.out.println("No");
                    break;
                } else {
                    magazineMap.remove(word);
                    magazineMap.put(word, num - 1);
                }
            } else {
                result = false;
                System.out.println("No");
                break;
            }
        }

        if (result)
            System.out.println("Yes");

        /*try {
            for (String word : note) {
                Integer num = magazineMap.get(word);
                if (num == 0) {
                    System.out.println("No");
                    return;
                } else {
                    magazineMap.remove(word);
                    magazineMap.put(word, num - 1);
                }
            }
            System.out.println("Yes");
        } catch (NullPointerException e) {
            System.out.println("No");
        }*/

    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String[] mn = scanner.nextLine().split(" ");

        int m = Integer.parseInt(mn[0]);

        int n = Integer.parseInt(mn[1]);

        String[] magazine = new String[m];

        String[] magazineItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < m; i++) {
            String magazineItem = magazineItems[i];
            magazine[i] = magazineItem;
        }

        String[] note = new String[n];

        String[] noteItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            String noteItem = noteItems[i];
            note[i] = noteItem;
        }

        checkMagazine(magazine, note);

        scanner.close();
    }
}
