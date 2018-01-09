#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;

struct Node
{
    Node *next;
    int value;
};

Node *chain;

void step(int steps)
{
    for (int i=0;i<steps;i++)
        chain = chain->next;
}


void insert(int value)
{
    Node *new_node = malloc(sizeof(Node));
    new_node->value = value;
    new_node->next = chain->next;
    chain = chain->next = new_node;
}

int read_()
{
    return chain->value;
}

void go_to(int value)
{
    while (chain->value != value)
        chain = chain->next;
}

int main()
{
    int steps = 376; //OMG, they haven't written anywhere that 376 is just number of steps....
    
    chain = malloc(sizeof(Node));
    chain->value = 0;
    chain->next = chain;
    
    for(int v=1; v <= 2017;v++)
    {
        step(steps);
        insert(v);
    }
    step(1);
    printf("part 1: %d\n",read_());
    
    return 0;
} 
