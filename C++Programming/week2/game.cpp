# include <iostream>
# include <string>
using namespace std;

int judge(int, int);

// 게임 흐름, 스트라이크/볼 처리 등을 다루는 함수들이 들어있다.
bool game(int answer) {
    int input;
    cout << "Enter a guess: ";
    cin >> input;
    if(judge(input, answer) == 3)
        return true;
    else
        return false;
}
int judge(int input, int answer) {
    int strikes = 0;
    int balls = 0;
    string i = to_string(input);
    string a = to_string(answer);

    for(int s = 0 ; s < 3 ; s++)
        for(int b = 0 ; b < 3 ; b++) {
            if(s == b && to_string(i[s]) == to_string(a[b])) {
                strikes++;
                break;
            }
            else if(i[s] == a[b])
                balls++;
    }
    cout << "Strikes: " << strikes << ", Balls: " << balls << endl;
    return strikes; 
}