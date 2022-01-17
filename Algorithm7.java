package Practice;

import java.util.ArrayList;

public class Algorithm7 {
	ArrayList<Integer> numList = new ArrayList<>();
	int basenum = 2;
	int count=1;
	Algorithm7(){
		while(numList.size() < 10001) {
			for(int i=2; i<basenum+1; i++) {
				if(basenum % i == 0) {
					count+=1;
				if(count == 3)
					break;
					}
				}
			if (count == 2)
				this.numList.add(basenum);
			this.count = 1;
			this.basenum += 1;
		}
	}
	public static void main(String[] args) {
		Algorithm7 a = new Algorithm7();
		System.out.println(a.numList.get(10000));
	}
}
