#include <stdio.h>

int main()
{
	char nama[5] = "Budi";
	char nama1[] = "Susi";
	int angka[] = {100, 200, 300};

	int i;
	for (i = 0; i < sizeof(nama)/sizeof(char); i++) {
		printf("%p: %c\n", &nama[i], nama[i]);
	}
	printf("\n");

	for (i = 0; i < sizeof(nama1)/sizeof(char); i++) {
		printf("%p: %c\n", &nama1[i], nama1[i]);
	}
	printf("\n");

	for (i = 0; i < sizeof(angka)/sizeof(int); i++) {
		printf("%p: %d\n", &angka[i], angka[i]);
	}
	printf("\n");

	// array pada dasarnya adalah mengalokasikan memory
	// dengan ukuran sesuai dengan tipe data dikali dengan
	// banyak item, char[5] = 5 bytes, int[3] = 12 bytes (4 bytes * 3)
	// array yang dirujuk tanpa nomor index, merujuk ke alamat memory
	// item pertama array tersebut
	
	printf("alamat memory nama: %p\n", nama);
	printf("alamat memory item 0 nama: %p\n\n", &nama[0]);

	// operator aritmatik pada pointer merupakan cara untuk mengakses
	// alamat memory tertentu sesuai ukuran tipe data pointer
	char *pnama = nama;

	printf("pnama: %p: %c\n", pnama, *pnama);
	printf("nama: %p: %c\n", nama, nama[0]);

	// next item
	printf("pnama: %p: %c\n", pnama+1, *(pnama+1));
	printf("nama: %p: %c\n", &nama[1], nama[1]);

	// next item
	printf("pnama: %p: %c\n", pnama+2, *(pnama+2));
	printf("nama: %p: %c\n\n", &nama[2], nama[2]);

	// untuk integer
	int *pangka = angka;

	// 3 banyak item array angka
	printf("%15s %15s %15s %15s\n", "alamat pangka", "nilai pangka", "alamat angka", "nilai angka");
	for (i = 0; i < 3; i++) {
		printf("%15p %15d %15p %15d\n", pangka+i, *(pangka+i), &angka[i], angka[i]);
	}

	return 0;
}
