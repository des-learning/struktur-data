#include <stdio.h>

// function
void swap(int *a, int *b) {
	int t;
	t = *b;
	*b = *a;
	*a = t;
}

int main()
{
	int angka = 10;
	// *pangka adalah pointer ke memory yang ditunjuk
	// oleh &angka
	int *p_angka = &angka;

	printf("angka: %d\n", angka);
	printf("&angka: %p\n", &angka);
	printf("p_angka: %p\n", p_angka);
	printf("*p_angka: %d\n", *p_angka);
	printf("&p_angka: %p\n", &p_angka);

	int angka1 = angka;

	angka1 = 20;
	printf("angka: %d, angka1: %d, *p_angka: %d\n",
			angka, angka1, *p_angka);
	*p_angka = 100;
	printf("angka: %d, angka1: %d, *p_angka: %d\n",
			angka, angka1, *p_angka);

	printf("angka: %d, angka1: %d\n", angka, angka1);
	swap(&angka, &angka1);
	printf("angka: %d, angka1: %d\n", angka, angka1);

	// tunggu sampai user menekan enter
	char enter[1024];
	scanf("%s", enter);

	return 0;
}
