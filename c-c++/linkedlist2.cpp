//Delete element at nth position
//Insert at the end
#include<stdio.h>
#include<stdlib.h>

struct Node
{
	int data;
	Node* next;
};

struct Node* head;

void Insert(int x, int n)
{
	//Node* temp1 = (Node*)malloc(sizeof(struct Node))   ---> c
	Node* temp1 = new Node(); //c++
	temp1->data = x;
	temp1->next = NULL;
	if(n==1)
	{
		temp1->next = head;
		head = temp1;
		return;
	}
	Node* temp2 = head;
	for(int i = 0;i<n-2;i++)
	{
		temp2 = temp2->next;
	}
	temp1->next = temp2->next;
	temp2->next = temp1;
}
void InsertAtFront(int x)
{
		Node* temp = (Node*)malloc(sizeof(struct Node));
		temp->data = x;
		temp->next = head;
		head = temp;
}
void InsertAtEnd(int x)
{
	//Node* temp = (Node*)malloc(sizeof(struct Node));
	Node* temp = new Node();
	temp->data = x;
	temp->next = NULL;
	if (head == NULL)
	{
		head = temp;
		return;
	}
	Node* temp1 = head;
	while(temp1->next!=NULL)
	{
		temp1 = temp1->next;
	}
	temp1->next = temp;
}

void Print()
{
	Node* temp = head;
	while(temp!=NULL)
	{
		printf("%d ",temp->data);
		temp = temp->next;
	}
	printf("\n");
}

void Delete(int n)
{
	Node* temp1 = head;
	if (n==1)
	{
		head = temp1->next;
		free(temp1);
		return;
	}
	int i;
	for (i=0;i<n-2;i++)
	{
		temp1 = temp1->next;
	}
	Node* temp2 = temp1->next;
	temp1->next = temp2->next;
	free(temp2);
}

void Reverse()
{
	Node* current = head;
	Node* next = current;
	Node* prev = NULL;
	while(next!=NULL)
	{	
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	head = prev;
}

void PrintRecursively(struct Node* p)
{
	if (p == NULL)
	{
		printf("\n");
		return;
	}
	printf("%d ",p->data);
	PrintRecursively(p->next);
}
//To-do print reverse using recursion

void ReverseRecursively()
{
	
}
int main()
{
	head = NULL;
	InsertAtEnd(1);
	InsertAtEnd(2);
	InsertAtEnd(3);
	InsertAtEnd(4);
	InsertAtEnd(5);
	Print();
	
}