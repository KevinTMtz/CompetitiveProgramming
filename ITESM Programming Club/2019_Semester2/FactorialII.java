import java.util.Scanner;

class FactorialII {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Cases:");
        int t = sc.nextInt();

        int[] arr = new int[t];

        for(int i = 0;i<t;i++) {
            arr[i] = sc.nextInt();
        }

        for(int i=0;i<t;i++){
            long zeros = 0;
            
            for(int k=5;(arr[i]/k)>=1;k*=5){
                zeros += (arr[i]/k); 
            }

            System.out.println(zeros);
        }
        sc.close();
    }
    
}