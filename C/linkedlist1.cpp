//Linked list: Insert elemets at nth position
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

void Print()
{
	Node* temp = head;
	while (temp!=NULL)
	{
		print("%d ",temp->data);
		temp = temp->next;
	}
	print("\n");
}


int main()
{
	head = NULL;
	Insert(1,1); //1
	Insert(2,2); //1,2
	Insert(5,1); //5,1,2
	Insert(4,2); //5,4,1,2
	Print();
}