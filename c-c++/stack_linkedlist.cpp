#include<stdio.h>
#include<stdlib.h>

struct Node
{
	int data;
	Node* next = NULL ;
};

struct Node* top = NULL;

void Push(int x)
{
	struct Node* temp = (Node*)malloc(sizeof(struct Node));
	temp->data = x;	
	temp->next = top;
	top = temp;
}

void Pop()
{
	struct Node* temp = (Node*)malloc(sizeof(struct Node));
	if (top == NULL)
	{
		printf("Stack is already Empty");
		return;
	}
	temp = top;
	top = temp->next;
	free(temp);
}

int Top()
{
	return top->data;
}

int main()
{
	Push(1);
	Push(2);
	printf("%d",Top());
	Pop();
	printf("%d",Top());
}