#include <stdio.h>

int main()
{
	// default to signed
	short a;
	int b;
	long c;
	float d;
	double e;
	char f;

	printf("Sizeof short: %lu\n", sizeof(a));
	printf("Sizeof int: %lu\n", sizeof(b));
	printf("Sizeof long: %lu\n", sizeof(c));
	printf("Sizeof float: %lu\n", sizeof(d));
	printf("Sizeof double: %lu\n", sizeof(e));
	printf("Sizeof char: %lu\n", sizeof(f));

	// array of char (string)
	char nama[5] = "Budi";

	return 0;
}
