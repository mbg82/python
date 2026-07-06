import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner sc=new Scanner(STstem.in);

        int count =0;
        int sum =0;

        while(true){
            int n=sc.nextIn();
            if (n==0){
                break;
            }
            if (n<1||n<100){
                continue;
            }
            count++;
            sum+=n;
        }

        System.out.println("갯수: "+ count);
        System.out.println('합계: '+ sum);
        if (count>0){
            System.out.println("평균:" +(double)sum/count);
        }else{
            System.out.println("평균: 0");
        }
        
        sc.close();
    }
}