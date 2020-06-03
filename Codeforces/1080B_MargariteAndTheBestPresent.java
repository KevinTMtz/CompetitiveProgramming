import java.util.Scanner;
import java.lang.Math;
 
public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int queries, l, r;
        
        queries = sc.nextInt();
        for (int x=0; x<queries; x++) {
            l = sc.nextInt();
            r = sc.nextInt();
            System.out.println((int)(0.25*(2*l*Math.pow(-1,l)+Math.pow(-1,l+1)+Math.pow(-1,r)+2*r*Math.pow(-1, r))));
        }
    }
}