#include <stdio.h>

int main()
{
	// deklarasikan angka sebagai variable dengan tipe int
	// dan inisialisasi dengan nilai 10
	int angka = 10;

	// deklarasi `int angka` mengalokasikan ruang memory untuk
	// menampung sebuah data int sesuai dengan ukuran int yaitu
	// 4 bytes (atau 2 bytes untuk yang mesin 16bit).

	printf("angka: %d\n", angka);
	// operator & di depan nama variable digunakan untuk merujuk
	// ke alamat memory yang telah dilokasikan sebelumnya (reference)
	printf("alamat memory angka: %p\n", &angka);

	// int * merupakan tipe pointer, pada contoh ini adalah
	// pointer ke sebuah alamat memory dengan ukuran int.
	// pointer merupakan tipe data khusus yang isinya adalah alamat
	// memory yang akan dituju.
	int *pangka;

	// pangka merujuk ke alamat angka
	pangka = &angka;

	// operator * pada contoh berikut adalah deference, digunakan untuk
	// mengakses nilai yang berada pada alamat memory yang dirujuk oleh
	// pointer bersangkutan
	printf("nilai di alamat memory yang dirujuk pangka: %d\n", *pangka);
	printf("alamat memory yang dirujuk pangka: %p\n", pangka);
	printf("alamat memory pangka: %p\n", &pangka);

	// mengubah nilai pada alamat memory yang dirujuk pangka
	*pangka = 100;
	printf("angka: %d\n", angka);
	printf("pangka: %d\n", *pangka);

	return 0;
}
