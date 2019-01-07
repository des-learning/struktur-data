# Pengenalan struktur data

## Satuan data/informasi

1. bit (binary digit), satuan informasi terkecil pada sistem komputer. Terdiri dari 2 variasi nilai, 0 dan 1.
2. byte, 8 bit, satuan terkecil yang dapat diolah oleh program.
3. kilobyte (kb), 1024 bytes (2<sup>10</sup> bytes)
4. megabyte (mb), 1024  kb
5. gigabyte (gb), 1024 mb
6. terabyte (tb), 1024 gb
7. petabyte (pb), 1024 tb

## Storage pada komputer

Terdiri dari primary dan secondary storage.

### Primary Storage

Primary storage (biasanya disebut RAM, random access memory) merupakan unit storage utama pada sistem komputer. CPU biasanya menggunakan primary storage sebagai tempat untuk menampung data yang akan dan sedang diolah serta hasil pengolahan.

1. Ukuran relatif lebih kecil dibanding secondary storage
2. Kecepatan baca/tulis lebih kencang dibanding secondary storage
3. *Velotile*, data/informasi yang berada di primary storage sifatnya hanya sementara. Data/informasi hanya disimpan ketika unit masih mendapatkan daya listrik.

### Secondary Storage

Secondary storage digunakan sebagai media penyimpanan yang sifatnya lebih permanen dibandingkan primary storage. Contoh secondary storage: punched card, tape, diskette, HDD, CD, DVD, flashdisk, SSD, dll.

1. Ukuran relatif lebih besar dibandingkan primary storage
2. Kecepatan baca/tulis relatif lebih lambat dibanding primary storage
3. *Semi velotile*, data/informasi akan tetap tersimpan walaupun unit tidak mendapatkan daya listrik.

## Tipe data

Tipe data dasar yang umum dijumpai pada bahasa pemrograman:

1. Number

   Terdiri dari bilangan bulat (Integer) dan bilangan pecahan (Float).

   * Bilangan bulat

     * byte - 1 byte range 0 - 255 unsigned, -128 - 127 signed
     * short - 2 bytes range 0 - 65535 unsigned, -32768 - 32768 signed
     * integer - 4 bytes range 0 - 2<sup>32</sup>-1 unsigned, -2<sup>31</sup> - 2<sup>31</sup>-1 signed
     * long - 8 bytes range 0 - 2<sup>64</sup> unsigned, -2<sup>63</sup> - 2<sup>63</sup>-1, signed

     Ukuran integer biasanya mengikuti platform (16bit, 32bit atau 64bit). Untuk angka yang signed (bertanda negatif/positif), range nya biasanya adalah -2<sup>bit</sup> - 2<sup>bit</sup>-1 yang di-*encode* menggunakan [**ones complement**](https://www.geeksforgeeks.org/find-ones-complement-integer/).

   * Bilangan pecahan

     Bilangan pecahan di-*encode* mengikuti standar [IEEE 754](https://www.geeksforgeeks.org/floating-point-representation-basics/). Representasi bilangan pecahan pada komputer dibatasi sampai presisi tertentu. Hal ini menyebabkan nilai pecahan atau operasi yang melibatkan bilangan pecahan kadang akan kehilangan nilai pada tingkat presisi tertentu.

     * float - 4 bytes, bilangan pecahan single-precision
     * double - 8 bytes, bilangan pecahan double-precision, memiliki jangkauan nilai lebih tinggi dibanding float.

2. Character

   Biasanya digunakan untuk menampung karakter [ASCII](https://en.wikipedia.org/wiki/ASCII). Ukuran storage character adalah 1 byte, menampung range angka dari 0 - 255.

   Pada bahasa C/C++, string merupakan array of character.

3. Boolean

   Menampung nilai `true`/`false`. Untuk bahasa pemrograman yang tidak memiliki tipe khusus (seperti C/C++) biasanya direpresentasikan menjadi nilai `int`, 0/negatif adalah untuk `false` dan bilangan positif untuk `true`.

4. Array

   Array merupakan struktur data paling sederhana, digunakan untuk menampung sekumpulan data dengan tipe tertentu (misalnya, array of int).