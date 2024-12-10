//
// Created by kabun  on 11/11/21.
//

#include <algorithm>
#include <iostream>
#include <list>
#include <string>

using namespace std;

bool MyCom(int v1,int v2)
{
    //降序：让第一个数大于第二个数
    return v1>v2;
}
//
//void Print(const list<int> &l)
//{
//    for(list<int>::const_iterator it = l.begin();it!=l.end();it++)
//    {
//         cout<< *it ;
//    }
//    cout << endl;
//}
//
//void test()
//{
//    list<int>l1;
//    l1.push_back(10);
//    l1.push_back(20);
////    Print(l1);
//    //拷贝构造
//    list<int>l2(l1);
//    list<int>l3(l1.begin(),l1.end());
//    list<int>l4(10,5);
////    Print(l2);
//
//    //赋值
//    l2=l4;
////    Print(l2);
//    l3.assign(l2.begin(),l2.end());
////    Print(l3);
//    l3.assign(3,6);
////    Print(l3);
//    //交换
//    l1.swap(l3);
////    Print(l1);
//    //大小操作
////    cout<< l1.size()<<endl;
//    l2.resize(20,10);//多余的用0填充
//    bool b = l1.empty();
////    cout <<b <<endl;
//    //删除 插入
//    l2.push_back(30);
//    l2.push_back(30);
//    l2.push_front(30);
//    l2.push_front(30);
////    Print(l2);
//    l2.pop_back();
//    l2.pop_front();
////    Print(l2);
//    list<int>::iterator it=l2.begin();
//    l2.insert(++it,1000);
////    Print(l2);
//    it = l2.begin();
//    l2.erase(it);
////    Print(l2);
//    l2.remove(5);
////    Print(l2);
//    l2.clear();
////    Print(l2);
//    //存取
//    //l2[3]//不可以，at也不可以，因为不是连续的线性空间，不能随机访问，
////    cout<<l3.front()<<endl;
////    cout<<l1.back()<<endl;
//    //排序
//    l2.push_back(1);
//    l2.push_back(4);
//    l2.push_back(2);
//    l2.push_back(5);
//    l2.push_back(3);
//    l2.reverse();//反转
//    Print(l2);
//    l2.sort();//排序:默认升序
//    Print(l2);
//    l2.sort(MyCom);//降序
//    Print(l2);
//    //下面是错误的，因为所有不支持随机访问迭代器的容器都不可以用标准算法
//    //不支持随机访问迭代器的容器内部会提供算法
//    //    sort(l2.begin(),l2.end());//错误
//
//}

//案例：按照年龄进行升序排列，如果年龄相同按照身高进行降序排列

class Person
{
public:
    string mname;
    int mage;
    int mhight;

    Person(string name,int age,int hight)
    {
        this->mage = age;
        this->mhight= hight;
        this->mname= name;
    }
};

//制定排序规则
bool PersonCom(Person &p1,Person &p2)
{
    //按照年龄升序

    if (p1.mage==p2.mage)
    {
        return p1.mhight>p2.mhight;
    }
    return p1.mage<p2.mage;
}

void Print(list<Person> &l)
{
    for(list<Person>::iterator it = l.begin();it!=l.end();it++)
    {
        cout<< "姓名  " <<(*it).mname
            <<"  年龄  "<<(*it).mage
            <<"  身高  "<<(*it).mhight<<endl;
    }
}

void test()
{
    list<Person> p;
    Person p1("asd",35,175);
    Person p2("asd",45,180);
    Person p3("asd",40,170);
    Person p4("asd",25,195);
    Person p5("asd",35,165);
    Person p6("asd",35,200);

    p.push_back(p1);
    p.push_back(p2);
    p.push_back(p3);
    p.push_back(p4);
    p.push_back(p5);
    p.push_back(p6);
//    for(list<Person>::iterator it = p.begin();it!=p.end();it++)
//    {
//        cout<< "姓名" <<(*it).mname
//        <<"年龄"<<(*it).mage
//        <<"身高"<<(*it).mhight ;
//    }
//    Print(p);
    p.sort(PersonCom);
    Print(p);
}


int main()
{
    test();
    return 0;
}