#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <inttypes.h>

void strcat_c(char *buf, char append)
{
    char *ptr = buf;
    for(; *ptr; ptr++);
    *ptr++ = append;
    *ptr = '\x00';
}

int main(void)
{
    char c;
    uint32_t min, max, sum;
    sum = 0;
    max = 0;
    min = 0xFFFFFFFF;
    
    char num [10];
    memset(num, 0, sizeof(num));
    while((c=getchar())!=EOF)
    {
        if(c == '\n')
        {
            int last = atoi(num);
            memset(num, 0, sizeof(num));
            
            if (last<min)
                min = last;
            if (last>max)
                max = last;
                
            sum += max-min;
            max = 0;
            min = 0xFFFFFFFF;
        }
        else if(c == ' ' || c == 0x09)
        {
            int last = atoi(num);
            memset(num, 0, sizeof(num));
            if (last<min)
                min = last;
            if (last>max)
                max = last;
        }
        else
        {
            strcat_c(num, c);
        }
    }
    printf("%d\n", sum);
    return 0;
} 
