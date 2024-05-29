#include <iostream>
using namespace std;
int main()
{
    string  a ,b,c;
    cout << "canh 1:";
    getline(cin, a);
    cout << "canh 2:";
    getline(cin, b);
    cout << "canh 3:";
    getline(cin, c);
    if (a + b > c )
    {
        cout << "yes";
    }
    else if (a + c > b)
    {
        cout << "yes";
    }
    else if (b + c > a)
    {
        cout << "yes";
    }
    else
    {
        cout << "no";
    }
    return 0;
}