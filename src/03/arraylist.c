#include <stdlib.h>
#include <string.h>

#include <stdio.h>

/*
 * List merupakan struktur data dasar yang digunakan untuk menampung
 * kumpulan data. Beda list dengan array adalah, list bersifat dinamis.
 * Dengan menggunakan list, programmer dapat menambahkan data terus-
 * menerus sebelum list-nya penuh. Programmer dapat menyisip data di tengah
 * atau menghapus data di tengah list, dan urutan data di dalam list akan
 * otomatis diatur ulang sehingga kumpulan data tetap bersebelahan tanpa
 * ada ruang kosong ditengah.
 *
 * operasi yang diimplementasikan:
 * newList(&list) -> membuat list baru
 * add(&list, item) -> menambahkan item baru ke akhir list
 * get(&list, index) -> mengakses item pada index tertentu dari list
 * set(&list, index, new_item) -> mengubah isi item index tertentu di list
 * removeItem(&list, index) -> menghapus item pada index tertentu dari list
 * insert(&list, index, new_item) -> menyisipkan item pada index tertentu di list
 * length(list) -> menghitung banyak item di list
 * deleteList(&list) -> menghapus list
 * capacity(list) -> berapa banyak kapasitas untuk list sekarang
 */

#define INITIAL_CAPACITY 10

typedef struct {
	int *items;
	int capacity;
	int size;
} List;

List *newList()
{
	List *l = (List *) malloc(sizeof(List));
	l->items = malloc(sizeof(int) * INITIAL_CAPACITY);
	l->capacity = INITIAL_CAPACITY;
	l->size = 0;
	return l;
}

void disposeList(List *l)
{
	free(l->items);
	free(l);
}

int length(const List *l)
{
	return l->size;
}

int capacity(const List *l)
{
	return l->capacity;
}

int indexValid(const List *l, int index)
{
	return index >= 0 && index < length(l);
}

int listFull(const List *l)
{
	return l->size >= l->capacity;
}

int get(const List *l, int index)
{
	if (indexValid(l, index)) {
		return l->items[index];
	}
	return -999999;
}

void growList(List *l)
{
	int new_capacity = capacity(l) + INITIAL_CAPACITY;
    int mem_size = sizeof(int) * new_capacity;
	int *titems = (int *) malloc(mem_size);
    memcpy(titems, l->items, mem_size);
	l->items = titems;
	l->capacity = new_capacity;
}

int add(List *l, int item)
{
	if (listFull(l)) {
		growList(l);
	}
	l->items[l->size] = item;
	l->size++;
	return 0;
}

int set(List *l, int index, int item)
{
	if (indexValid(l, index)) {
		l->items[index] = item;
		return 1;
	}
	return 0;
}

int removeItem(List *l, int index)
{
	if (indexValid(l, index)) {
		for (int i = index+1; i < length(l); i++) {
			set(l, i-1, get(l, i));
		}
		l->size--;
		return 1;
	}
	return 0;
}

int insert(List *l, int index, int item)
{
	if (indexValid(l, index)) {
		if (listFull(l)) {
			growList(l);
		}
		for (int i = length(l); i >= index; i--) {
			l->items[i+1] = l->items[i];
		}
		l->items[index] = item;
		l->size++;
		return 1;
	}
	return 0;
}

void display(List *l)
{
	printf("List capacity: %d\n", capacity(l));
	printf("List length: %d\n", length(l));
	printf("List data:\n");
	for (int i = 0; i < length(l); i++) {
		printf("%d - %d\n", i, get(l, i));
	}
}

int main()
{
	List *l = newList();
	int a[] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000};

	for (int i = 0; i < sizeof(a)/sizeof(int); i++) {
		add(l, a[i]);
	}
	display(l);

	printf("data pertama: %d\n", get(l, 0));
	printf("data terakhir: %d\n", get(l, length(l) - 1));

	set(l, 3, 99);
	display(l);

	removeItem(l, 3);
	display(l);

	insert(l, 0, 2000);
	insert(l, 0, 4000);
	insert(l, 0, 8000);
	insert(l, 0, 16000);
	display(l);

	disposeList(l);
	char c;
	scanf("%c", &c);
	return 0;
}
