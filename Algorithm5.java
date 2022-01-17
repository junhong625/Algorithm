package Practice;

public class Algorithm5 {
	int count;
	int num = 2520;
	Algorithm5(){
		while(count != 20) {
			num += 1;
			for(int i=1; i<21; i++) {
				if(num % i == 0)
					count += 1;
				else {
					count = 0;
					break;
				}
			}
		}
	}
	public static void main(String[] args) {
		Algorithm5 a = new Algorithm5();
		System.out.println(a.num);
	}
}
