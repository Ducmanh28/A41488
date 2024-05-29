#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    float cannang;
    float chieucao;
    float BMI = cannang / pow(chieucao, 2);
    cout << "nhap chieu cao:";
    cin >> chieucao;
    cout << "nhap can nang:";
    cin >> cannang;
    cout << "chi so BMI cua ban la:" << BMI << endl;
    return 0;
}