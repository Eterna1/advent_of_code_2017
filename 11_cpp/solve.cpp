#include <iostream>
#include <cstdio>
#include <cmath>
#include <boost/algorithm/string.hpp> //trim //sudo apt-get install libboost-dev


using namespace std;

int count_steps(int pos_x, int pos_y)
{
    if(pos_y>pos_x)
    {
        return pos_x + ((pos_y-pos_x)/2);
    }
    else
    {
        return pos_x;
    }
}

int main(int argc, char **argv)
{
    int pos_y = 0; //pionowy , vertical
    int pos_x = 0; //poziomy, horizontal
    
    string direction;
    
    int steps;
    int max_steps = 0;
    
    while (getline(std::cin, direction, ','))
    {
        boost::trim_right(direction); //there are trim_right, trim_left, trim in boost
        //cout<<"direction :"<<direction<<endl;
        
        if (direction == "n")
        {
            pos_y-= 2;
        }
        else if (direction == "s")
        {
            pos_y += 2;
        }
        else if (direction == "ne")
        {
            pos_y -- ;
            pos_x ++ ;
        }
        else if (direction == "nw")
        {
            pos_y -- ;
            pos_x -- ;
        }
        else if (direction == "sw")
        {
            pos_y ++ ;
            pos_x -- ;
        }
        else if (direction == "se")
        {
            pos_y ++ ;
            pos_x ++ ;
        }
        
        steps = count_steps(pos_x, pos_y);
        max_steps = max(steps, max_steps);
    }
    
    cout <<"currently we are at position ("<<pos_x<<","<<pos_y<<")"<<endl;
    
    //compute the steps from 0;0 to pos_vertical;pos_horizontal
    //hmmm, to count the number of steps it really does not matter in which quarter we are.
    pos_y = abs(pos_y);
    pos_x = abs(pos_x);
    
    //is this point above the diagonal?
    if(pos_y>pos_x)
    {
        steps = pos_x + ((pos_y-pos_x)/2);
    }
    else
    {
        steps = pos_x;
    }
    
    cout<<"steps to ending position: "<<steps<<endl;
    cout<<"steps to furthest postiion: "<<max_steps<<endl;
    return 0;
}
 
