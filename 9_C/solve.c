#include <stdio.h>
#include <stdbool.h>

int main()
{
    bool in_garbage = false;
    bool after_exclamation = false;
    
    int current_group_score = 0;
    int groups;
    int score = 0;
    int chars_in_garbage = 0;
    
    char c;
    while ((c = getchar()) != EOF)
    {
        if (in_garbage)
        {
            if (c=='>' && !after_exclamation)
            {
                in_garbage = false;
            }
            else if (c=='!' && !after_exclamation)
            {
                after_exclamation = true;
                chars_in_garbage --;
            }
            else
            {
                chars_in_garbage ++;
                after_exclamation = false;
            }
        }
        else
        {// we are not in a garbage currently
            if (c == '{')
            {
                current_group_score ++;
                groups ++;
                score += current_group_score;
            }
            else if (c == '}')
            {
                current_group_score --;
            }
            else if (c == '<')
            {
                in_garbage = true;
            }
        }
    }
    
    printf("number of groups: %d\n", groups);
    printf("total score: %d\n", score);
    printf("chars in garbage: %d\n", chars_in_garbage);
    
    return 0;
} 
