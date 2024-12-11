//
// Created by kabun on 2021/11/17.
//

#include <algorithm>
#include <iostream>
#include <set>
#include <string>

using namespace std;
class MyCom
{
public:
    bool operator()(int v1,int v2)
    {
        return v1>v2;
    }
};
class Person
{
public:
    string mname;
    int mage;
    int mhight;

    Person(string name,int age,int hight)
    {
        this->mname= name;
        this->mage = age;
        this->mhight= hight;
    }
};
class PersonCom
{
public:
    bool operator()(const Person &p1,const Person &p2)
    {
        return p1.mage > p2.mage;
    }
};

void Print(set<int,MyCom> &l)
//void Print(set<int> &l)
//void Print(set<Person,PersonCom> &l)
//void Print(multiset<int> &l)
{
//    for(set<int>::iterator it = l.begin();it!=l.end();it++)
//    for(set<Person,PersonCom>::iterator it = l.begin();it!=l.end();it++)
    for(set<int,MyCom>::iterator it = l.begin();it!=l.end();it++)
//    for(multiset<int>::iterator it = l.begin();it!=l.end();it++)
    {
         cout<< *it <<"  ";
//        cout<< it->mname <<"  "<< it->mage <<"  "<< it->mhight <<"  "<<endl;
    }
    cout << endl;
}

void test()
{
    set<int,MyCom> s;
    //插入只有insert
    s.insert(10);
    s.insert(50);
    s.insert(30);
    s.insert(20);
    s.insert(30);
    Print(s);
//
//    //拷贝构造
////    set<int> s2(s);
//    set<int> s3;
//    set<int> s5;
//    s5.insert(666);
    //赋值
//    s3=s2;
    //大小
//    cout<<s.size() <<endl;
//    cout<<s.empty() <<endl;
//    swap(s,s5);
//    s5.swap(s);
//    Print(s5);
    //插入删除
//    s3.erase(20);
////    Print(s3);
//    set<int>::iterator it=s3.begin();
//    it++;
//    s3.erase(it);
////    Print(s3);
//    s3.clear();
//    set<int>::iterator pos=s5.find(30);//返回的是迭代器
////    cout << s5.count(20) << endl;//统计
////    cout << *pos << endl;
//    pair<set<int>::iterator,bool> ret = s.insert(666);
//    Print(s);
//    if(ret.second)
//    {
//        cout << "win";
//    }
//    else
//    {
//        cout<<"lose";
//    }

//    multiset<int> ms;
//    ms.insert(30);
//    ms.insert(30);
//    Print(ms);
//}

//pair
//void test01()
//{
//    pair<string,int> p("zhangzan",18);
//    cout << p.first<<p.second <<endl;
//    pair<string,int> p2 = make_pair("jrlly",118);
//    cout << p2.first<<p2.second <<endl;
}

//void test02()
//{
//    set<Person,PersonCom> p;
//    Person p1("asd",35,175);
//    Person p2("asd",45,180);
//    Person p3("asd",40,170);
//    Person p4("asd",25,195);
//    Person p5("asd",35,165);
//    Person p6("asd",35,200);
//    p.insert(p1);
//    p.insert(p2);
//    p.insert(p3);
//    p.insert(p4);
//    p.insert(p5);
//    p.insert(p6);
//    Print(p);
//
//}
int main()
{
    test();
//    test01();
//    test02();
    return 0;
}