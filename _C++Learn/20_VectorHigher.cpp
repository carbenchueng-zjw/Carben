//
// Created by kabun  on 11/7/21.
//
#include <iostream>
#include <vector>
//#include <string>
#include <algorithm>//标准算法的头文件
using namespace std;

void Print(vector<int> &v)
{
    for(vector<int>::iterator it = v.begin();it!=v.end();it++)
    {
        cout<< *it<<"  ";
    }
    cout <<endl;
}

void test()
{
    vector<int> v;//默认构造
    for(int i =0;i<10;i++)
    {
        v.push_back(i);//尾插
    }
//    Print(v);
//
//    //通过区间方式构造
//    vector<int> v2(v.begin(),v.end());
//    Print(v2);
//
//    //n个elem方式构造
//    vector<int> v3(10,100);
//    Print(v3);
//
//    //拷贝构造
//    vector<int> v5(v3);
//    Print(v5);

    //判断是否为空
//    if(v.empty())
//    {
//        cout<< "里面没有东西" <<endl;
//    }
//    else
//    {
//        cout<< "里面有东西" <<endl;
//        cout<< "容量："<<v.capacity() <<endl;
//        cout<< "大小："<<v.size() <<endl;
//    }
//    v.resize(20,66);
//    v.resize(3);//超出的部分会删除
//    Print(v);
//    cout<< "容量："<<v.capacity() <<endl;

//    插入和删除
//    v.pop_back();//尾删
//    Print(v);
//    v.insert(v.begin(),100); //插入，第一个参数是迭代器
//    Print(v);
//    v.insert(v.end(),2,66); //插入，第一个参数是迭代器
//    Print(v);
//    v.erase(v.begin());//删除
////    v.erase(v.begin(),v.end());//区间删除
//    Print(v);
//    v.clear();//清空
//    Print(v);

    //存取
//    for(int i=0;i<v.size();i++)
//    {
//        cout << v[i] <<"  ";
////        cout << v.at(i) <<"  ";
//    }
//    cout << v.front() <<endl;//获取第一个
//    cout << v.back() <<endl;//获取最后一个

    //互换容器(收缩内存空间)
//    vector<int> te(6,66);
//    v.swap(te);
//    Print(v);
//    cout<< "容量："<<v.capacity() <<endl;
//    v.resize(3);
//    vector<int>(v).swap(v);//收缩内存空间
//    cout<< "容量："<<v.capacity() <<endl;
//    cout<< "大小："<<v.size() <<endl;

    //预留空间（减少动态扩展时的扩展次数）
    vector<int> hh;
    hh.reserve(1000);
    int num=0;
    int *p = NULL;
    for (int i=0;i<1000;i++)
    {
        hh.push_back(i);
        if(p!=&hh[0])
        {
            p=&hh[0];
            num++;
        }
    }
    cout << num;
}

int main()
{
    test();
    return 0;
}