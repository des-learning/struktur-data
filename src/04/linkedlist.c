#include <stdlib.h>
#include <stdio.h>

typedef struct Node {
	int value;
	struct Node *next;
} Node;

typedef struct LinkedList {
	Node *head;
	Node *tail;
	int length;
} LinkedList;

LinkedList *newList()
{
	LinkedList *list = (LinkedList *) malloc(sizeof(LinkedList));
	list->head = NULL;
	list->tail = NULL;
	list->length = 0;
	return list;
}

int length(LinkedList *list)
{
	return list->length;
}


Node *newNode(int value)
{
	Node *node = (Node *) malloc(sizeof(Node));
	node->value = value;
	node->next = NULL;
	return node;
}

void disposeNode(Node *node)
{
	free(node);
}

int indexValid(LinkedList *list, int index)
{
	return index >= 0 && index < length(list);
}

Node *gotoIndex(LinkedList *list, int index)
{
	if (indexValid(list, index)) {
		Node *currentNode = list->head;
		int c = 0;
		while (currentNode != NULL) {
			if (c == index) {
				return currentNode;
			}
			currentNode = currentNode->next;
			c++;
		}
	}
	return NULL;
}

void removeItem(LinkedList *list, int index)
{
	if (indexValid(list, index) && index == 0) {
		Node *node = list->head;
		list->head = node->next;
		disposeNode(node);
		list->length--;
	} else {
		Node *node = gotoIndex(list, index-1);
		if (node != NULL) {
			Node *tmp = node->next;
			node->next = tmp->next;
			disposeNode(node);
			if (index == list->length-1) {
				list->tail = node;
			}
			list->length--;
		}
	}
}

void disposeList(LinkedList *list)
{
	// remote all items
	while (length(list) > 0) {
		removeItem(list, 0);
	}
	free(list);
}




int add(LinkedList *list, int value)
{
	Node *node = newNode(value);

	// list kosong
	if (list->head == NULL) {
		list->head = node;
		list->tail = node;
	// list berisi
	} else {
		list->tail->next = node;
		list->tail = node;
	}
	list->length++;
}

int get(LinkedList *list, int index)
{
	Node *node = gotoIndex(list, index);
	if (node != NULL) {
		return node->value;
	}
	return -9999999;
}

void set(LinkedList *list, int index, int value)
{
	Node *node = gotoIndex(list, index);
	if (node != NULL) {
		node->value = value;
	}
}



void insertItem(LinkedList *list, int index, int value)
{
	if (indexValid(list, index) && index == 0) {
		Node *node = newNode(value);
		node->next = list->head;
		list->head = node;
		list->length++;
	} else {
		Node *node = newNode(value);
		Node *ptr = gotoIndex(list, index-1);
		if (ptr != NULL) {
			Node *tmp = ptr->next;
			node->next = tmp;
			ptr->next = node;
			list->length++;
		}
	}
}

void displayList(LinkedList *list)
{
	Node *cur = list->head;
	while (cur) {
		printf("%d\n", cur->value);
		cur = cur->next;
	}
}

int main()
{
	LinkedList *list = newList();
	printf("Add 10, 20\n");
	add(list, 10);
	add(list, 20);
	displayList(list);

	printf("set(0, 99)\n");
	set(list, 0, 99);
	displayList(list);

	printf("insert(1, 30), insert(0, 40), insert(3, 50)\n");
	insertItem(list, 1, 30);
	insertItem(list, 0, 40);
	insertItem(list, 3, 50);
	displayList(list);
	disposeList(list);
	return 0;
}
