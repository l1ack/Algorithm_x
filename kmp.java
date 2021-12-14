import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class kmp {
    public static int strStr(String haystack, String needle) {
        int n = haystack.length(), m = needle.length();
        if (m == 0) {
            return 0;
        }
        int[] pi = new int[m];
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && needle.charAt(i) != needle.charAt(j)) {
                j = pi[j - 1];
            }
            if (needle.charAt(i) == needle.charAt(j)) {
                j++;
            }
            pi[i] = j;
        }
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && haystack.charAt(i) != needle.charAt(j)) {
                j = pi[j - 1];
            }
            if (haystack.charAt(i) == needle.charAt(j)) {
                j++;
            }
            if (j == m) {
                return i - m + 1;
            }
        }
        return -1;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str1 = new String();
        String str2 = new String();
        System.out.println("Enter lines of text.");
        System.out.println("Enter 'end' to quit.");
        str1 = br.readLine();
        str2 = br.readLine();
        // do {
        //     try {
        //         str = br.readLine();
        //     } catch (IOException e) {
        //         // TODO Auto-generated catch block
        //         e.printStackTrace();
        //     }
        //     System.out.println(str);
        // } while (!str.equals("end"));
        int t;
        t=strStr(str1, str2);
        System.out.print(t);
    }
}
