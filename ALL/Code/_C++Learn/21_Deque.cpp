//
// Created by kabun  on 11/9/21.
//
#include <iostream>
#include <deque>
//#include <string>
#include <algorithm>//标准算法的头文件
using namespace std;


void Print(const deque<int> &r)
{
    for(deque<int>::const_iterator it=r.begin();it!=r.end();it++)
    {
//        *it = 100;//容器中的数据不可以修改
        cout <<*it<<"  ";
    }
    cout <<endl;
}

void test()
{
    deque<int> d1;
    deque<int> d2;
//    for(int i =0;i<10;i++)
//    {
//        d1.push_back(i);
////        cout << d1[i]<<"  ";
//    }
//    Print(d1);
//
//    deque<int> d2(d1);
//    Print(d2);
//
//    deque<int> d3(d1.begin(),d1.end());
//    Print(d3);
//
//    deque<int> d5(12,3);
//    Print(d5);

    //赋值
//    d2=d1;
//    d1.assign(3,3);
//    d2.assign(d1.begin(),d1.end());
//    Print(d1);

    //大小
//    bool f = d1.empty();
//    cout << f <<endl;
//    cout << d1.size() <<endl;
//    d1.resize(2,3);
//    d1.resize(2);
//    cout << d1.size() <<endl;

    //插入和删除
    //插入
    d1.assign(3,6);
//    d1.push_front(20);
//    d1.push_back(10);
//    Print(d1);
//    d1.pop_front();
//    d1.pop_back();
//    Print(d1);
    d1.insert(d1.begin(),30);
    d1.insert(d1.end(),2,20);
    d2.insert(d2.begin(),d1.begin(),d1.end());
    Print(d1);
    Print(d2);

    //删除
//    deque<int>::iterator it = d1.begin();
//    it++;
//    d1.erase(d1.begin()+5);
//    d1.erase(d1.begin(),d1.end());
//    d1.clear();
//    Print(d1);

//    存取
//    cout << d1[2]<<endl;
//    cout << d1.at(5)<<endl;
//    cout << d1.front()<<endl;
//    cout << d1.back()<<endl;

    //排序
    sort(d1.begin(),d1.end());//默认升序
    Print(d1);
}


int main()
{

    test();
    return 0;
}