#include <stdio.h>

// parameter array 2D dikirimkan dengan menggunakan pointer
// pada dasarnya array 2D pada memory dialokasikan dalam bentuk
// stream memory yang contiguous/saling berdampingan
// representasi visual:
// +---+---+---+---+---+
// |0,0|0,1|0,2|0,3|0,4|
// +---+---+---+---+---+
// |1,0|1,1|1,2|1,3|1,4|
// +---+---+---+---+---+
// |2,0|2,1|2,2|2,3|2,4|
// +---+---+---+---+---+
//
// alokasi di memory:
// +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
// |0,0|0,1|0,2|0,3|0,4|1,0|1,1|1,2|1,3|1,4|2,0|2,1|2,2|2,3|2,4|
// +---+---+---+---+---+---+---+---+---+---+---+---+---+---+---+
void add(int *angka, int baris, int kolom, int x)
{
	for (int i = 0; i < baris; i++) {
		for (int j = 0; j < kolom; j++) {
			angka[i*kolom+j] = angka[i*kolom+j]+x;
		}
	}
}

int main()
{
	// array 2 dimensi, dimensi pertama 3,
	// dimensi kedua 5
	int angka[3][5] = {{ 1, 2, 3, 4, 5},
					   { 6, 7, 8, 9,10},
					   {11,12,13,14,15}};
	int i, j;

	for (i = 0; i < 3; i++) {
		for (j = 0; j < 5; j++) {
			printf("%2d ", angka[i][j]);
		}
		printf("\n");
	}
	printf("=====\n");

	add(&angka[0][0], 3, 5, 10);
	for (i = 0; i < 3; i++) {
		for (j = 0; j < 5; j++) {
			printf("%2d ", angka[i][j]);
		}
		printf("\n");
	}

	return 0;
}
