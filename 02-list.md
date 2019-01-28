# List

List merupakan struktur data dasar yang menampung kumpulan item data.

Operasi umum pada list:

- `create(list)`: membentuk list baru
- `dispose(list)`: menghapus list (membebaskan resource memory yang digunakan oleh list)
- `add(list, value)` atau `append(value)`: menambahkan value baru ke akhir list
- `get(list, index)`: mengembalikan item list pada posisi index (dihitung dari index 0)
- `set(list, index, value)`: mengubah isi list pada posisi index dengan item baru
- `remove(list, index)`: menghapus item pada posisi index
- `length(list, index)`: menghitung jumlah item pada list
- `insert(list, index, value)`: menyisipkan item baru pada posisi index

Implementasi List:

- [`ArrayList`](arraylist.md) untuk akses menggunakan index dengan waktu konstan

- [`LinkedList`](linkedlist.md) untuk operasi `insert` pada awal/akhir list secara konstan dan `remove` item dengan efisien