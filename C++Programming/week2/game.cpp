# include <iostream>
# include <string>
using namespace std;

int judge(string, string);

// 게임 흐름, 스트라이크/볼 처리 등을 다루는 함수들이 들어있다.
bool game(string answer) {
    string input;
    cout << "Enter a guess: " << ends;
    cin >> input;
    if(judge(input, answer) == 3)
        return true;
    else
        return false;
}

int judge(string input, string answer) {
    int strikes = 0;
    int balls = 0;

    for(int s = 0 ; s < 3 ; s++)
        for(int b = 0 ; b < 3 ; b++) {
            if(s == b && input[s] == answer[b])
                strikes++;
            else if(input[s] == answer[b])
                balls++;
    }

    cout << "Strikes: " << strikes << ", Balls: " << balls << endl;
    return strikes; 
}