import java.io.*;
import java.math.*;
import java.text.*;
import java.util.*;
import java.util.regex.*;

public class Solution {

    /*
     * Complete the timeConversion function below.
     */
    static String timeConversion(String s) {
        String[] timeArray = s.split(":");

        if(timeArray[0].equals("12")){
            timeArray[0] = "00";
        }

        if (timeArray[2].indexOf("PM") > 0) {
            timeArray[0] = Integer.toString(Integer.parseInt(timeArray[0]) + 12);
        }

        timeArray[2] = timeArray[2].substring(0, 2);

        return timeArray[0] + ":" + timeArray[1] + ":" + timeArray[2];
    }

    private static final Scanner scan = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bw = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String s = scan.nextLine();

        String result = timeConversion(s);

        bw.write(result);
        bw.newLine();

        bw.close();
    }
}
