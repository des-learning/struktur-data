#include <stdio.h>

// int sum(int angka[], int n) // by value
int sum(int *angka, int n)	// by reference
{
	int total = 0;
	int i;
	for (i = 0; i < n; i++) {
		//total += *(angka+i);
		total += angka[i];
	}
	return total;
}

int main()
{
	int angka[5] = { 10, 20, 30, 40, 50 };
	int i;
	int *p_angka = angka;	 // int *p_angka = &angka[0];

	for (i = 0; i < 5; i++) {
		//printf("angka[%d]: %d\n", i, angka[i]);
		printf("angka[%d]: %d\n", i, *(p_angka+i));
	}
	printf("Total: %d\n", sum(angka, 5));
	return 0;
}
