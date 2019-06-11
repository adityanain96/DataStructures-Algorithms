#include<stdio.h>
#include<stdlib.h>

struct Node
{
	int data;
	Node* next;
	Node* prev;
};

struct Node* head; //global variable - pointer to head node

struct Node* GetNewNode(int x)
{
	struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
	newNode->data = x;
	newNode->prev = NULL;
	newNode->next = NULL;
	return newNode;
};

void InsertAtHead(int x)
{
	struct Node* newNode = GetNewNode(x);
	if(head == NULL)
	{
		head = newNode;
		return;
	}
	head->prev = newNode;
	newNode->next = head;
	head = newNode;
}

void InsertAtTail(int x)
{
	struct Node* newNode = GetNewNode(x);
	if(head == NULL)
	{
		head = newNode;
		return;
	}
	Node* temp = head;
	while(temp->next!=NULL)
	{
		temp = temp->next;
	}
	temp->next = newNode;
	newNode->prev = temp;
	newNode->next = NULL;
}

void PrintForward()
{
	Node* temp = head;
	while (temp!=NULL)
	{
		printf("%d ",temp->data);
		temp = temp->next;
	}
}

int main()
{
	head = NULL;
	InsertAtHead(1);
	InsertAtHead(2);
	InsertAtHead(3);
	InsertAtHead(4);
	PrintForward();
	InsertAtTail(5);
	InsertAtTail(6);
	InsertAtTail(7);
	PrintForward();
}