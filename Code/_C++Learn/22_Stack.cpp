//
// Created by kabun  on 11/10/21.
//
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <time.h>
using namespace std;

void test()
{
    stack<int> stk;
    stk.push(10);
    stk.push(20);
    stk.push(30);
//    stack<int> stk1(stk);//拷贝构造

    cout << stk.size()<<endl;
    //只要栈不为空就查看栈顶
    while(!stk.empty())
    {
        //查看
        cout<<stk.top()<<endl;
        //出栈
        stk.pop();
    }

    cout << stk.size();
}

int main()
{
    test();
    return 0;
}