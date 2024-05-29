#include <iostream>
using namespace std;
int main()
{
    int a;
    cout << "nhap khoa ban hoc:";
    cin >> a;
    for (int i = 0; i <= a; i++)
    {
        if (a % i == 0 && a % 3 == 1)
        {
            cout << i << " ";
     
        }
    }
    return 0;
}