#include <iostream>
using namespace std;

bool game(string);
string randomThree();

// 게임을 실제로 실행시키는 main() 함수가 들어있는 메인 파일이다.
int main() {
    string answer = randomThree();
    while(true) {
        if(game(answer))
            break;
    }
    cout << "You win!" << endl;
}