package com.ajh.practice;

public class Algorithm4 {
	int maxNum;
	Algorithm4(){
		for(int i = 999; i > 100; i--) {
			for(int j = 999; j > 100; j--) {
				String result = String.valueOf(i*j)  ;
				int num = 0;
				for(int idx = 0 ; idx < result.length()/2; idx++) {
					if (result.charAt(idx)!=result.charAt(result.length()-idx-1)) {
						num = 0;
						break;}
					else
						num += 1;
				}
				if (num == 3)
					if (maxNum < i*j)
						maxNum = i*j;
			}
		}
	}
	public static void main(String[] args) {
		Algorithm4 a = new Algorithm4();
		System.out.println(a.maxNum);
	}
}
