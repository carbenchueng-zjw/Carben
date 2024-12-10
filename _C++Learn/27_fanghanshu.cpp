//
// Created by kabun on 2021/11/22.
//

#include <functional>
#include <vector>
#include <ctime>
#include <iostream>
using namespace std;

//基础仿函数
//class MyAdd
//{
//public:
//    int operator()(int v1,int v2)
//    {
//        return v1+v2;
//    }
//};
//
//class MyPrint
//{
//public:
//    int count;
//    MyPrint()
//    {
//        this->count=0;
//    }
//    void operator()(string v1)
//    {
//        cout << v1;
//        this->count++;
//    }
//};
//
//void doprint(MyPrint &p,string contect)
//{
//    p(contect);
//}

//void test()
//{
    //    MyAdd add;
//    MyPrint pring;
//    pring("asdasd");
//    cout << pring.count;
//    MyPrint print;
//    doprint(print,"what???");
//    cout << add(10,20);
//}

//内建仿函数对象：算术仿函数
//negate 一元仿函数，取反仿函数
//void test01()
//{
//    negate<int> n;
//    cout<<n(50)<<endl;
//}
//
////plus 二元仿函数 加法
//void test02()
//{
//    plus<int> p;
//    cout<<p(50,10)<<endl;
//}

//关系仿函数
//void test01()
//{
//    vector<int> v;
//    v.push_back(10);
//    v.push_back(30);
//    v.push_back(20);
//    sort(v.begin(),v.end(),greater<int>());
//    for(vector<int>::iterator it=v.begin();it!=v.end();it++)
//    {
//        cout << "找到了："<<*it;
//    }
//    cout<<endl;
//}

//逻辑仿函数
void test()
{
    vector<bool> v;
    v.push_back(true);
    v.push_back(false);
    v.push_back(true);
//    sort(v.begin(),v.end(),greater<int>());
    for(vector<bool>::iterator it=v.begin();it!=v.end();it++)
    {
        cout << "找到了："<<*it;
    }
    cout<<endl;

    //逻辑取反
    vector<bool> v2;
    v2.resize(v.size());
    transform(v.begin(),v.end(),v2.begin(),logical_not<bool>());
    for(vector<bool>::iterator it=v2.begin();it!=v2.end();it++)
    {
        cout << "找到了："<<*it;
    }
    cout<<endl;
}

int main()
{
//    srand((unsigned int)time(NULL));
//    int ss = rand()%110;
//    cout << ss<<endl;

    test();
//    test01();
//    test02();

    return 0;
}