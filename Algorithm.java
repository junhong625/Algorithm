package com.ajh.practice;

public class Algorithm {
	static int result = 0;
	static void numSum(int num) {
		for (int i = 1; i < num; i++) {
			if (i % 3 == 0 || i % 5 == 0) {
				result += i;
			}
		}
		System.out.println(result);
	}
	public static void main(String[] args) {
		numSum(1000);
	}
}