#include <stdio.h>
#include <string.h>
#include <stdlib.h>
//#include <inttypes.h>

void strcat_c(char *buf, char append)
{
    char *ptr = buf;
    for(; *ptr; ptr++);
    *ptr++ = append;
    *ptr = '\x00';
}

typedef struct Node Node;

typedef struct Node
{
    Node *next;
    int num;
} Node;

//typedef struct Node Node;

Node *node = NULL;

void free_nodes()
{
    Node *node_i = node;
    Node *node_next;
    
    if (node_i)
    {
        node_next = node_i->next;
        free(node_i);
        node_i = node_next;
    }
}

void new_nodes(void)
{
    free_nodes();
    
    node = NULL;
}

void add_node(int num)
{
    Node *new_node = malloc(sizeof(Node));
    new_node->num = num;
    new_node->next = node;
    node = new_node;
}

int divides_evenly(int num)
{
    Node *node_i = node;
    while(node_i)
    {
        if (num % node_i->num == 0)
            return num / node_i->num;
        if (node_i->num % num == 0)
            return node_i->num / num;
            
        node_i = node_i->next;
    }
    return -1;
}

int main(void)
{
    char c;
    int min, max, sum;
    sum = 0;
    
    char num [10];
    memset(num, 0, sizeof(num));
    while((c=getchar())!=EOF)
    {
        if(c == '\n')
        {
            int last = atoi(num);
            memset(num, 0, sizeof(num));
            
            int div = divides_evenly(last);
            
            if (div!=-1)
                sum += div;
            
            new_nodes();
           
        }
        else if(c == ' ' || c == 0x09)
        {
            int last = atoi(num);
            memset(num, 0, sizeof(num));
            
            int div = divides_evenly(last);
            
            if (div!=-1)
                sum += div;
              
                
            add_node(last);
        }
        else
        {
            strcat_c(num, c);
        }
    }
    printf("%d\n", sum);
    return 0;
} 
