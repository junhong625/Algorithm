package Practice;

public class Algorithm9 {
	public static void main(String[] args) {
	int result = 0;
	for(int i=0; i<333; i++)
		for(int j=i; j<666; j++)
			for(int k=j; k<998;k++) {
				if (i<j & j<k) 
					if (i+j+k == 1000) 
						if(i*i+j*j==k*k) {
							result = i*j*k;
							break;
			}		
		}		
	System.out.println(result);
	}
}
