package com.ajh.practice;

public class Algorithm10 {
	int result;
	Algorithm10(){
		for(int i = 0; i > 2000001; i++) {
			int count = 0;
			for(int j =1; j > i+1; j++) {
				if (i % j == 0)
					count += 1;
				if (count == 3)
					break;
			if (count == 2)
				result += i;
			}
		}
	}public static void main(String[] args) {
		Algorithm10 a = new Algorithm10();
		System.out.println(a.result);
	}
}
