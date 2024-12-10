//
// Created by kabun  on 11/10/21.
//

#include <algorithm>
#include <iostream>
#include <queue>
#include <string>
#include <stack>
#include <time.h>
using namespace std;

class Player
{
public:
    int m_score;
    string m_name;
    Player(string name,int score)
    {
        this->m_name = name;
        this->m_score = score;
    }
};

void test()
{
    queue<Player> stk;
    Player p1("大",10);
    Player p2("中",20);
    Player p3("小",30);

    stk.push(p1);
    stk.push(p2);
    stk.push(p3);

    cout << stk.size()<<endl;
    //只要栈不为空就查看栈顶
    while(!stk.empty())
    {
        //查看队头
        cout<<stk.front().m_name<<endl;
        //查看队尾
        cout<<stk.back().m_name<<endl;
        //出队
        stk.pop();
    }

    cout << stk.size();
}

int main()
{
    test();
    return 0;
}