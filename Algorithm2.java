package com.ajh.practice;

public class Algorithm2 {
	int result = 0;
	Algorithm2(int num1, int num2, int num){
		while (num1 <num || num2 < num) {
			if (num1 % 2 == 0) 
				result += num1;
			num1 += num2;
			if (num2 % 2 == 0) 
				result += num2;
			num2 += num1;
		}
	}
	public static void main(String[] args) {
		Algorithm2 a = new Algorithm2(1, 2, 4000000);
		System.out.println(a.result);
	}
}
