#include <iostream>
using namespace std;
int main()
{
    int a, b;
    cout << "nhap so thu nhat:";
    cin >> a;
    cout << "nhap so thu hai:";
    cin >> b;
    if (a > b)
    {
        cout << "a is greater than b";
    }
    else if (a < b)
    {
        cout << " a is smaler than b";
    }
    else
    {
        cout << " a is equal to b";
    }
    return 0;
}