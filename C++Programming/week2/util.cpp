#include <string>
#include <random>
#include <chrono>
using namespace std;

// 숫자 랜덤 생성을 다루는 함수가 들어있다.
string randomThree() {
    string answer = "";
    // 0 ~ 9 사이의 난수를 발생시키는 코드
    unsigned seed = chrono::system_clock::now().time_since_epoch().count();
    mt19937 gen(seed);
    uniform_int_distribution<std::mt19937::result_type> dist(0, 9);

    for(int i = 0 ; i < 3 ; i++) {
        while(true) {
            string next = to_string(dist(gen));
            // 넣으려는 난수가 이미 있는 수가 아닌 경우 (중복 X)
            if(answer.find(next) == string::npos) {
                answer.append(next);
                break;
            }
        }
    }

    return answer;
}