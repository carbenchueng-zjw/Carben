//
// Created by kabun on 2021/11/22.
//
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

class Person
{
public:
    string mname;
    int mscore;
    Person(string name,int score)
    {
        mname = name;
        mscore = score;
    }
    //重栽 ==
    bool operator==(const Person& p)
    {
//        if(this->mname==p.mname && this->mscore==p.mscore)
        if(this->mscore==p.mscore)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};

class ForEach
{
public:
    bool operator()(int val)
    {
        cout<<val<<"  ";
    }
};

class GreatFive
{
public:
    bool operator()(int val)
    {
        return val>5;
    }
};

class Great20
{
public:
    bool operator()(Person &val)
//    bool operator()(int val)
    {
//        return val>20;
        return val.mscore>20;
    }
};

class TransForm
{
public:
    int operator()(int val)
    {
        return val+100;
    }
};

void print(int val)
{
    cout<<val<<"  ";
}

class MyPrint
{
public:
    void operator()(int v1)
    {
        cout<< v1 <<"  ";
    }
//    cout <<endl;
};

void test()
{
    vector<int> vfe;
    vfe.push_back(10);
    vfe.push_back(30);
    vfe.push_back(20);
    vfe.push_back(20);
    vfe.push_back(30);
    vfe.push_back(50);
    vector<Person> p;
    Person p1("zhansan",10);
    Person p2("asdsan",20);
    Person p3("iiiiii",30);
    Person px("iiasdi",10);
    p.push_back(p1);
    p.push_back(p2);
    p.push_back(p3);
    //for_each
//    for_each(vfe.begin(),vfe.end(), print);
//    cout<<endl;
//    for_each(vfe.begin(),vfe.end(), ForEach());

    //transform
//    vector<int> vtf;
//    vtf.resize(vfe.size());
//    transform(vfe.begin(),vfe.end(),vtf.begin(),TransForm());
//    for_each(vtf.begin(),vtf.end(), MyPrint());
//    cout<<endl;

//查找：：
    //find
//    vector<int>::iterator it = find(vfe.begin(),vfe.end(),30);
//    cout<<*it<<endl;

//    vector<Person>::iterator ss = find(p.begin(),p.end(),p3);
//    cout<<ss->mname<<ss->mscore<<endl;
//    //find_if
//    vector<int>::iterator iff = find_if(vfe.begin(),vfe.end(),GreatFive());
//    cout<<*iff<<endl;
//    vector<Person>::iterator pff = find_if(p.begin(),p.end(),Great20());
//    cout<<pff->mname<<endl;
//    //adjacent_find//查找相邻重复的元素
//    vector<int>::iterator iajf = adjacent_find(vfe.begin(),vfe.end());
//    cout<<*iajf<<endl;
    //binary_search//返回真假,必须是有序的序列，不然结果有问题，会有误
//    bool bs = binary_search(vfe.begin(),vfe.end(),30);
//    cout<<bs<<endl;

//    count//统计元素个数，返回int
//    int vc = count(vfe.begin(),vfe.end(),20);
//    int pvc = count(p.begin(),p.end(),px);
//    cout<<vc<<endl;
//    cout<<pvc<<endl;
//    count_if()
//    int vci =  count_if(vfe.begin(),vfe.end(),Great20());
//    int pci =  count_if(p.begin(),p.end(),Great20());
//    cout<<vci<<endl;
//    cout<<pci<<endl;

//排序：：
//    sort

}


int main()
{
    test();
    return 0;
}
