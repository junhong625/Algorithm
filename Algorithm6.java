package Practice;

public class Algorithm6 {
	int result;
	int sum;
	Algorithm6(){
		for(int i=1; i<101; i++) {
			result += i*i;
			sum += i;
		}
	}
	public static void main(String[] args) {
		Algorithm6 a = new Algorithm6();
		System.out.println(a.sum * a.sum - a.result);
	}
}
