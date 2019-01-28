## ArrayList

Implementasi List menggunakan array. Pada dasarnya array bersifat static yaitu jumlah item yang bisa ditampung harus dideklarasikan pada saat compile. Supaya array dapat menampung item dengan jumlah dinamis, implementasi ArrayList pada C/C++ dilakukan dengan menggunakan alokasi memory dinamis (`malloc`/`new`).

Struktur data:

    ArrayList:
    - capacity(int): kapasitas penyimpanan ArrayList
    - values(array[capacity]): menampung data ArrayList
    - length(int): jumlah item yang tersimpan pada ArrayList

Algoritma:

- `create(list)`

  bentuk struktur data ArrayList baru dengan nilai awal: `{capacity: 10, values: [], length: 0}`. Nilai `capacity` ditentukan sesuai kebutuhan.

- `dispose(list)`

  bebaskan resource memory, set `capacity` ke nilai awal (10), `values` ke `[]` dan `length` ke 0.

- `add(list, value)`

  1. jika kapasitas masih mencukupi (`length < capacity`), tambahkan `value` ke `values[length]` dan `length = length + 1`.

  2. jika kapasitas tidak mencukupi (`length >= capacity`), jalankan prosedur `grow(list)` untuk menambah `capacity` ArrayList. Tambahkan `item` ke `values[length]` dan `length = length + 1`

- `get(list, index)`

  1. jika `index` valid (`index >= 0 && index < length`), kembalikan nilai `values[index]`

  2. jika `index` invalid, kembalikan error (invalid index)

- `set(list, index, value)`

  1. jika `index` valid (`index >= 0 && index < length`), kembalikan ubah nilai `values[index]` menjadi `value`

  2. jika `index` invalid, kembalikan error (invalid index)

- `remove(list, index)`

  1. jika `index` valid (`index >= 0 && index < length`), geser seluruh item dari `values[index+1] sampai values[length-1]` ke sebelah kiri 1 posisi.

  2. jika `index` invalid, kembalikan error (invalid index)

- `length(list)`

  kembalikan nilai `length` dari struktur ArrayList

- `insert(list, index, value)`

  1. jika kapasitas masih mencukupi (`length < capacity`), geser seluruh item dari `values[index] sampai values[length]` ke sebelah kanan 1 posisi, set nilai `values[index]` ke `value`

  2. jika kapasitas tidak mencukupi, jalankan prosedur `grow(list)`, ulangi langkah 1.

Tambahan:

- `grow(list)`

  menambah kapasitas ArrayList, yaitu dengan mengalokasikan memory baru dengan kapasitas lebih besar dari kapasitas ArrayList yang sekarang, dan kemudian salin seluruh data ArrayList lama ke ArrayList baru.

- `indexValid(list, index)`

  kembalikan hasil evaluasi `index >= 0 && index < length`