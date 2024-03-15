#include <iostream>
using namespace std;

bool game(string);
string randomThree();

// 게임을 실제로 실행시키는 main() 함수가 들어있는 메인 파일이다.
int main() {
    string answer = randomThree();
    int wrong = 0;
    for(; wrong < 5 ; wrong++) {
        cout << 5-wrong << " chances left." << endl;
        if(game(answer)) {
            cout << "You win!" << endl;
            break;
        }   
    }
    if(wrong == 5) {
        cout << "You lose!" << endl;
    }
    
}