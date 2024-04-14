#include <iostream>
using namespace std;

bool arr[21] = {false};

bool Check(int x)
{
    return arr[x] == 1;
}

void Add(int x)
{
    if (!Check(x))
    {
        arr[x] = 1;
    }
}

void Remove(int x)
{
    if(Check(x))
    {
        arr[x] = 0;
    }
}

void Toggle(int x)
{
    if(!Check(x))
    {
        arr[x] = 1;
    }
    else
    {
        arr[x] = 0;
    }
}

void Empty()
{
    for (int i = 1; i < 21; i++)
        {
            arr[i] = 0;
        }
}

void All()
{
    for (int i = 1; i < 21; i++)
        {
            arr[i] = 1;
        }
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int x = 0;
    int t = 0;

    cin >> t;
    

    for (int i = 0; i < t; i++)
        {
            char str[8];
            cin >> str;

            if (str[0] == 'a' && str[1] == 'd') 
            {
                cin >> x;
                Add(x);
            }
            else if (str[0] == 'c') 
            {
                cin >> x;
                cout << Check(x) << "\n";
            }
            else if (str[0] == 'r') 
            {
                cin >> x;
                Remove(x);
            }
            else if (str[0] == 't') 
            {
                cin >> x;
                Toggle(x);
            }
            else if (str[0] == 'e') 
            {
                Empty();
            }
            else
            {
                All();
            }
        }

    return 0;
}