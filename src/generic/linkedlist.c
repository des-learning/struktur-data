#include <stdlib.h>
#include <string.h>
#include <stdio.h>

/* Singly Linked List dengan generic type
 * void * merupakan pointer ke alamat memory tanpa
 * diproses dengan ukuran tipe data tertentu,
 * mis. int * berarti pointer merujuk ke alamat memory
 * yang menampung nilai int.
 * sedangkan void * merujuk ke alamat memory tanpa
 * interpretasi nilai tertentu. Supaya dapat digunakan
 * nilai yang dirujuk oleh pointer void * harus di-casting
 * ke tipe tertentu */

typedef struct Node {
	// isi node adalah void *, tanpa interpretasi tipe tertentu
	void *content;
	struct Node *next;
} Node;

typedef struct LinkedList {
	Node *head;
	Node *tail;
	// ukuran memory untuk content yang ditampung masing-masing node
	int size;
	int length;
} LinkedList;

Node *NewNode(void *content, int size)
{
	// bentuk node baru
	Node *newNode = (Node *) malloc(sizeof(Node));
	newNode->next = NULL;
	// alokasikan memory untuk isi node (sebesar size dari linkedlist)
	newNode->content = (void *) malloc(size);
	// salin data ke content node
	memcpy(newNode->content, content, size);
	return newNode;
}

void DisposeNode(Node *node)
{
	// jangan lupa untuk bebaskan memory yang dialokasikan untuk content node
	free(node->content);
	// bebaskan memory node
	free(node);
}

LinkedList *NewList(int size)
{
	LinkedList *list = (LinkedList *) malloc(size);

	list->size = size;
	list->length = 0;
	list->head = NULL;
	list->tail = NULL;

	return list;
}

void DisposeList(LinkedList *list)
{
	Node *current = list->head;

	while (current != NULL) {
		Node *t = current;
		current = current->next;
		DisposeNode(t);
	}
	
	free(list);
}

void Add(LinkedList *list, void *content)
{
	Node *newNode = NewNode(content, list->size);
	if (list->head == NULL) {
		list->head = newNode;
		list->tail = newNode;
	} else {
		list->tail->next = newNode;
		list->tail = newNode;
	}
	list->length++;
}

int Length(LinkedList *list)
{
	return list->length;
}

int IsEmpty(LinkedList *list)
{
	return list->length == 0;
}

int IndexValid(LinkedList *list, int index)
{
	return index >= 0 && index < list->length;
}

// kembalikan node jika index valid, NULL jika tidak
Node *GotoIndex(LinkedList *list, int index)
{
	if (!IndexValid(list, index)) return NULL;

	Node *current = list->head;
	
	for (int i = 0; i < index; i++) {
		if (current == NULL) return NULL;
		current = current->next;
	}

	return current;
}

void *Get(LinkedList *list, int index)
{
	Node *node = GotoIndex(list, index);
	if (node == NULL) return NULL;
	// kembalikan content node
	return node->content;
}

void Remove(LinkedList *list, int index)
{
	if (index == 0 && IndexValid(list, index)) {
		Node *nextNode = list->head->next;
		DisposeNode(list->head);
		list->head = nextNode;
		list->length--;
	} else {
		Node *prevNode = GotoIndex(list, index-1);
		if (prevNode != NULL) {
			Node *node = prevNode->next;
			Node *nextNode = node != NULL ? node->next : NULL;
			prevNode->next = nextNode;
			DisposeNode(node);
			list->length--;
		}
	}
}

typedef struct Manusia {
	char *nama;
	int umur;
} Manusia;

void Display(LinkedList *list)
{
	for (int i =0; i < Length(list); i++) {
		// casting void * ke Manusia * dan ambil nilainya dengan
		// operator * (deference)
		Manusia m = *(Manusia *)Get(list, i);
		printf("%s, %d\n", m.nama, m.umur);
	}
	printf("\n");
}

int main()
{
	// list menampung item Manusia
	LinkedList *list = NewList(sizeof(Manusia));
	Manusia d[] = {
		(Manusia){"Budi", 20},
		(Manusia){"Susi", 19},
		(Manusia){"Andri", 27}
	};

	for (int i = 0; i < sizeof(d)/sizeof(Manusia); i++) {
		Add(list, &d[i]);
	}

	Display(list);

	Remove(list, 1);
	Display(list);

	DisposeList(list);
	return 0;
}
