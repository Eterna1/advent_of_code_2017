//g++ solve.cpp -o solve -std=c++11

#include <iostream>
#include <cstdio>
#include <vector>
#include <string> //stol()

using namespace std;

int main()
{
    std::vector<long> offsets;
    
    string num;
    while(std::getline(std::cin, num))
    {
        offsets.push_back(std::stol(num, NULL));
    }
    int counter = 0;
    int size = offsets.size();
    int steps = 0;
    
    while(counter<size && counter>=0)
    {
        int diff;
        if (offsets[counter] >= 3)
            diff = -1;
        else
            diff = 1;
        
        offsets[counter] += diff;
        counter = counter +  offsets[counter] - diff;
        steps++;
    }
    
    printf("%d\n", steps);
    
    return 0;
} 
