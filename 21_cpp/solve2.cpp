#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm> //for std::count
#include <inttypes.h>
#include <map>
#include <cstring>

#define K (0b111+1) //binary format

using namespace std;

void sort(uint64_t *tab, int size)
{
    bool changed = true;
    while (changed)
    {
        changed = false;
        for (int i=1;i<size;i++)
        {
            if (tab[i-1]>tab[i])
            {
                changed = true;
                uint64_t tmp = tab[i-1];
                tab[i-1] = tab[i];
                tab[i] = tmp;
            }
        }
    }
} 

uint64_t bin(char c)
{
    return (c == '#')? 1 : 0;
}

uint64_t hash_k_(string k)
{
    uint64_t hash = 0;
    for (int i=0;i<k.length();i++)
    {
        hash = hash*2 + bin(k[i]);
    }
    return hash;
}

uint64_t hash_k(string k)
{
    uint64_t a = hash_k_(k);
    std:reverse(k.begin(), k.end());
    uint64_t b = hash_k_(k);
    return min(a, b);
}

uint64_t hash2(string pattern) //compute hash for 2*2 square. The hash is the same after rotating and fliping the square. 
{
    string k1, k2, k3, k4;
    
    k1 = string(1, pattern[0]) + pattern[1];
    k2 = string(1, pattern[1]) + pattern[3];
    k3 = string(1, pattern[2]) + pattern[3];
    k4 = string(1, pattern[0]) + pattern[2];
    
    uint64_t h[4];
    h[0] = hash_k(k1);
    h[1] = hash_k(k2);
    h[2] = hash_k(k3);
    h[3] = hash_k(k4);
    
    sort(h, 4);
    
    uint64_t hash = 0;
    for (int i=0;i<4;i++)
    {
        hash = hash * K + h[i];
    }
    
    return hash;
}

uint64_t hash3(string pattern) //compute hash for 3*3 square. The hash is the same after rotating and fliping the square.
{
    string k1, k2, k3, k4;
    
    k1 = string(1,pattern[0]) + pattern[1] + pattern[2];
    k2 = string(1,pattern[2]) + pattern[5] + pattern[8];
    k3 = string(1,pattern[6]) + pattern[7] + pattern[8];
    k4 = string(1,pattern[0]) + pattern[3] + pattern[6];
    
    uint64_t h[4];
    h[0] = hash_k(k1);
    h[1] = hash_k(k2);
    h[2] = hash_k(k3);
    h[3] = hash_k(k4);
        
    sort(h, 4);
       
    uint64_t k = 0;
    for (int i=0;i<4;i++)
    {
        k = k * K + h[i];
    }
    
    k1 = string(1, pattern[1]) + pattern[4] + pattern[7];
    k2 = string(1, pattern[3]) + pattern[4] + pattern[5];
    h[0] = hash_k (k1);
    h[1] = hash_k (k2);
    sort(h, 2);
    
    k = k*K + h[0];
    k = k*K + h[1];
    
    k1 = string(1,pattern[3]) + pattern[0] + pattern[1];
    k2 = string(1,pattern[1]) + pattern[2] + pattern[5];
    k3 = string(1,pattern[3]) + pattern[6] + pattern[7];
    k4 = string(1,pattern[7]) + pattern[8] + pattern[5];
    
    h[0] = hash_k(k1);
    h[1] = hash_k(k2);
    h[2] = hash_k(k3);
    h[3] = hash_k(k4);
    
    sort(h, 4);
    
    for (int i=0;i<4;i++)
    {
        k = k * K + h[i];
    }
    
    return k;
}

void parse_rule_2(string line, map<uint64_t,string> &m)
{
    string end = "";
    end = end + line[9]+line[10]+line[11]+line[13]+line[14]+line[15]+line[17]+line[18]+line[19];
    string beginning = "";
    beginning = beginning + line[0]+line[1]+line[3]+line[4];
    uint64_t hash = hash2(beginning);
    
    if (m.count(hash) > 0)
    {
        cout<<"parse_rule_2!. hash collision!"<<endl;
        exit(0);
    }
    //m.insert ( std::pair<uint64_t,string>(hash,end) );
    m[hash] = end;
}

void parse_rule_3(string line, map<uint64_t,string> &m)
{
    string end = "";
    end = end + line[15]+line[16]+line[17]+line[18]+line[20]+line[21]+line[22]+line[23]; //pomidor
    end = end + line[25]+line[26]+line[27]+line[28]+line[30]+line[31]+line[32]+line[33];

    string beginning = "";
    beginning = beginning + line[0]+line[1]+line[2]+line[4]+line[5]+line[6]+line[8]+line[9]+line[10];
    uint64_t hash = hash3(beginning);
    
    if (m.count(hash)>0)
    {
        cout<<"parse_rule_3!. hash collision!"<<endl;
        exit(0);
    }
    m[hash] = end;
}

char at(char *array, int size, int x, int y)
{
    return array[x*size+y];
}

int a(int size, int x, int y)
{
    return x*size+y;
}

int main()
{
    string line;
    
    map<uint64_t,string> map2;
    map<uint64_t,string> map3;
    
    while(getline(cin, line))
    {
        int slashes_num = std::count(line.begin(), line.end(), '/');
        if (slashes_num == 3)
        {
            parse_rule_2(line, map2);
        }
        else if (slashes_num == 5)
        {
            parse_rule_3(line, map3);
        }
    }
    
    //
    
    int size = 3;
    char *array = new char[size*size];
    memcpy(array, ".#...####", 9);
    for(int i=0;i<18;i++)
    {
        int new_size;
        if(size % 2 == 0)
            new_size = size/2*3;
        else
            new_size = size/3*4;
            
        char *new_array = new char[new_size*new_size];
        
        if (size%2==0)
        {
            int squares = size/2;
            
            for(int x=0;x<squares;x++)
            for(int y=0;y<squares;y++)
            {
                string k = string(1, at(array,size,x*2,y*2)) + at(array,size,x*2,y*2+1)
                            +at(array,size,x*2+1,y*2) + at(array,size,x*2+1,y*2+1);
                
                                    
                uint64_t h = hash2(k);
                if (map2.count(h)==0)
                {
                    cout<<"hash not found: "<<k<<endl;
                    exit(4);
                }
                string new_val = map2[h];
                
                
                memcpy(&new_array[x*3*new_size + y*3], new_val.substr(0, 3).c_str(), 3);
                memcpy(&new_array[(x*3+1)*new_size + y*3], new_val.substr(3, 3).c_str(), 3);
                memcpy(&new_array[(x*3+2)*new_size + y*3], new_val.substr(6, 3).c_str(), 3);
            }
        }
        else if (size%3 == 0)
        {
            int squares = size/3;
            
            for(int x=0;x<squares;x++)
            for(int y=0;y<squares;y++)
            {
                string k = string(1, at(array,size,x*3,y*3)) + at(array,size,x*3,y*3+1) + at(array,size,x*3,y*3+2)
                    + at(array,size, x*3+1, y*3) + at(array,size, x*3+1, y*3+1) + at(array,size, x*3+1, y*3+2)
                    + at(array,size, x*3+2 ,y*3) + at(array, size, x*3+2, y*3+1) + at(array, size, x*3+2, y*3+2);
                 
                    
                uint64_t h = hash3(k);
                if (map3.count(h)==0)
                {
                    cout<<"hash not found: "<<k<<endl;
                    exit(2);
                }
                string new_val = map3[h];  
                memcpy(&new_array[x*4*new_size + y*4], new_val.substr(0, 4).c_str(), 4);
                memcpy(&new_array[(x*4+1)*new_size + y*4], new_val.substr(4, 4).c_str(), 4);
                memcpy(&new_array[(x*4+2)*new_size + y*4], new_val.substr(8, 4).c_str(), 4);
                memcpy(&new_array[(x*4+3)*new_size + y*4], new_val.substr(12, 4).c_str(), 4);
            }
        }
        else
        {
            cout<<"error at: "<<__LINE__;
            exit(3);
        }
        
        delete []array;
        size = new_size;
        array = new_array;
    }
    
    int on_count = 0;
    
    //print the array and count the pixels that are "on".
    for(int x=0;x<size;x++)
    {
        for(int y=0;y<size;y++)
        {
            char c = at(array,size,x,y);
            //cout<<c;
            if (c=='#')
                on_count++;
        }
        //cout<<endl;
    }
    
    cout<<on_count<<endl;
    
    delete[] array;
    return 0;
} 
