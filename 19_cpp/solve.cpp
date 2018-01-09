#include <cstdio>
#include <iostream>
#include <fstream>
#include <vector>

#define FILE "input.txt"

using namespace std;

int main()
{
    ifstream f;
    f.open(FILE);
    if (!f.is_open())
        return 1;
    
    vector<string> map;
        
    string line;    
    while (getline(f, line))
        map.push_back(line);
        
        
    int x = 0;
    int y = 0;
    int direction_x = 0;
    int direction_y = 1;
        
    //find start position
    for(x=0; map[0][x]!='|'; x++);
    
    string solution = "";
    int steps = 0;
    
    while (true)
    {
        char c = map[y][x];
        
        if (c == ' ')
            break;
        else if (c == '+')
        {
            if (direction_x == 0)
            {
                direction_y = 0;
                direction_x = (map[y][x+1] != ' ')? 1 : -1;
            }
            else
            {
                direction_x = 0;
                direction_y = (map[y+1][x] != ' ')? 1 : -1;
            }
        }
        else if (c >= 'A' && c <= 'Z')
        {
            solution += c;
        }
        
        x += direction_x;
        y += direction_y;
        steps += 1;
    }
    
    cout<<solution<<endl;
    cout<<"steps :"<<steps<<endl;
} 
