## LinkedList

Linked List terdiri dari Node yang dihubungkan dengan Node-Node berikutnya di dalam Linked List. Ada beberapa jenis Linked List, yang paling dasar adalah _Singly Linked List_ dan _Doubly Linked List_.

Struktur Data:

    Node:
    - value: menampung data yang akan disimpan di LinkedList
    - next: menyimpan reference ke Node berikutnya di dalam LinkedList, nilai defaultnya adalah NULL

    LinkedList:
    - head: menyimpan reference ke Node pertama pada LinkedList, jika LinkedList kosong, head masih merujuk ke NULL
    - tail: menyimpan reference ke Node terakhir pada LinkedList, jika LinkedList kosong, tail masih merujuk ke NULL
    - length: menyimpan jumlah item di dalam LinkedList, nilai awalnya adalah 0

Algortima:

- `create(list)`

  bentuk LinkedList baru, set `head` & `tail` ke `NULL` dan `length` ke 0

- `dispose(list)`

  `remove` seluruh item pertama (`head`) sampai LinkedList kosong, bebaskan resource memory

- `add(list, value)`

  1. Bentuk Node baru (`newNode`) isikan dengan `value`

  2. Jika LinkedList masih kosong:
      - `head` & `tail` LinkedList merujuk ke `newNode`

  3. Jika Linkedlist sudah terisi (`length > 0`):
      - hubungukan `tail` ke `newNode`, `tail.next = newNode`

  4. Naikkan counter panjang LinkedList, `length = length + 1`

- `get(list, index)`

  1. Jika `index` valid, `gotoIndex(index)` dan kembalikan value dari `Node` bersangkutan

  2. Jika `index` invalid, kembalikan error (invalid index)

- `set(list, index, value)`

  1. Jika `index` valid, `gotoIndex(index)` dan ubah nilai `Node.value` menjadi `value`

  2. Jika `index` invalid, kembalikan error (invalid index)

- `remove(list, index, value)`

  1. Jika `index == 0` (yang dihapus adalah Node `head`), pindahkan `head` ke `head.next`

  2. Jika `index  == length - 1` (yang dihapus adalah Node `tail`), pindahkan posisi baca (`currentNode`) ke posisi sebelum Node yang akan dihapus, `gotoIndex(index-1)`. Terminasi `currentNode`, `currentNode.next = NULL`. Pindahkan `tail` ke `currentNode`, `tail = currentNode`

  3. Jika `index` > 0 dan `index` valid, pindahkan posisi baca (`currentNode`) ke posisi sebelum Node yang akan dihapus, `gotoIndex(index-1)`. Hubungkan `currentNode` dengan `Node` berikutnya dari `Node` yang akan dihapus, `currentNode.next = currentNode.next.next`.

  4. Kurangi panjang list, `length = length - 1`

  5. Jika index invalid, return error (invalid index)

- `length(list)`

  kembalikan `length`

- `insert(list, index, value)`

  1. bentuk Node baru `newNode` dengan nilai `value`

  2. jika `index` == 0 (insert pada posisi `head`), hubungkan `newNode` dengan `head`, `newNode.next = head`. Pindahkan `head` ke `newNode`, `head = newNode`

  3. jika `index` > 0 dan `index` valid, pindahkan posisi baca (`currentNode`) ke posisi sebelum `index`, `gotoIndex(index-1)`. Hubungkan `newNode` dengan Node setelah `currentNode`, `newNode.next = currentNode.next`. Hubungkan `currentNode` dengan `newNode`, `currentNode.next = newNode`

  4. Tambah panjang list, `length = length + 1`