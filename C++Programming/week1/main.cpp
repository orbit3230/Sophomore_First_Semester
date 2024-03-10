#include <iostream>

int sum2(int a, int b);
int sub2(int a, int b);
int mul2(int a, int b);
int div2(int a, int b);

using namespace std;

int main() {
    int a;
    int b;
    cout << "A: ";
    cin >> a;
    cout << "B: ";
    cin >> b;

    cout << a << " + " << b << " = " << sum2(a, b) << endl;
    cout << a << " - " << b << " = " << sub2(a, b) << endl;
    cout << a << " * " << b << " = " << mul2(a, b) << endl;
    cout << a << " / " << b << " = " << div2(a, b) << endl;
}