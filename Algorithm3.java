package com.ajh.practice;

public class Algorithm3 {
	int maxNum = 0;
	public Algorithm3(long num) {
		int i = 2;
		while (num != 1) {
			if (num % i == 0) {
				num /= i;
				maxNum = i;}
			else
				i += 1;
		}
	}public static void main(String[] args) {
		Algorithm3 a = new Algorithm3(600851475143L);
		System.out.println(a.maxNum);
	}
}
