#include<stdio.h>
#include<stdlib.h>

struct Node
{
	int data;
	Node* next;
};

struct Node* front = NULL;
struct Node* rear = NULL;

void Enqueue(int x)
{
	struct Node* temp = (Node*)malloc(sizeof(struct Node));
	temp->data = x;
	temp->next = NULL;
	if (front == NULL && rear == NULL)
	{
		front = temp;
		rear = temp;
		return;
	}
	rear->next = temp;
	rear = temp;
}
void Print()
{
	struct Node* temp = (Node*)malloc(sizeof(struct Node));
	temp = front;
	while(temp!=NULL)
	{
		printf("%d ",temp->data);
		temp = temp->next;
	}
}

void Dequeue()
{
	struct Node* temp = (Node*)malloc(sizeof(struct Node));
	if (front == NULL)
	{
	    return;
	}
	if (front == rear)
	{
	    front = NULL;
	    rear = NULL;
	    return;
	}
	temp = front;
	front = temp->next;
	free(temp);
	
}

int main()
{
	Enqueue(1);
	Enqueue(2);
	Enqueue(3);
	Print();
	Dequeue();
	Print();
}