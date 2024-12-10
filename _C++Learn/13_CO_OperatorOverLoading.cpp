//
// Created by kabun  on 10/15/21.
//
#include <iostream>
#include <string>
using namespace std;

//加号运算符重载
//1：成员函数加号运算符重载
//class PERSON
//{
//public:
////    PERSON operator+(PERSON &p)
////    {
////        PERSON temp;
////        temp.m_a = this->m_a+p.m_a;
////        temp.m_b = this->m_b+p.m_b;
////        return temp;
////    }
//    int m_a;
//    int m_b;
//
//};
//
////2：全局函数加号运算符重载
//PERSON operator+(PERSON &p1,PERSON &p2)
//{
//    PERSON temp;
//    temp.m_a = p1.m_a+p2.m_a;
//    temp.m_b = p1.m_b+p2.m_b;
//    return temp;
//}
//
//void test01()
//{
//    PERSON p1;
//    p1.m_a = 10;
//    p1.m_b = 10;
//    PERSON p2;
//    p2.m_b = 10;
//    p2.m_a = 10;
//    PERSON p3;
//    p3 = p1+p2;
//    cout <<p3.m_a<<p3.m_b;
//}
//int main()
//{
//    test01();
//    return 0;
//}

//左移运算符重载
//class PERSON
//{
//    friend ostream &operator<<(ostream &out,PERSON &p);
//
//public:
//    PERSON(int a,int b)
//    {
//        m_a= a;
//        m_b= b;
//    }
//private:
//
//    int m_a;
//    int m_b;
//};
//ostream &operator<<(ostream &out,PERSON &p)
//{
//    out << p.m_a << endl;
//    out << p.m_b << endl;
//    return out;
//}
//void test01()
//{
//    PERSON p3(20,10);
//    cout <<p3 <<endl;
//
//}
//int main()
//{
//    test01();
//    return 0;
//}

//递增运算符重载
//class MYINTEGER
//{
//    friend ostream& operator<<(ostream& out,MYINTEGER myinteger);
//public:
//    MYINTEGER()
//    {
//        m_num=0;
//    }
////    前置递增
//    MYINTEGER &operator++()//返回引用是因为为了对本身进行操作，可以做链式法则
//    {
//        m_num++;
//        return *this;
//    }
//
////    后置递增
//    MYINTEGER operator++(int)//代表占位参数，区分前置后置递增
//    {
//        MYINTEGER temp = *this;
//        m_num++;
//        return temp;
//    }
//
//
//private:
//    int m_num;
//};
//
//ostream& operator<<(ostream& out,MYINTEGER myinteger)
//{
//    out <<myinteger.m_num;
//    return out;
//}
//
//void test01()
//{
////    MYINTEGER myinteger;
////    cout << ++(++myinteger) <<endl;
////    cout << myinteger <<endl;
//
//    MYINTEGER myinteger;
//    cout << myinteger++ <<endl;
//    cout << myinteger <<endl;
//}
//
//
//int main()
//{
//    test01();
//    return 0;
//}


//赋值运算符重载
//class PERSON
//{
//public:
//    PERSON(int num)
//    {
//        m_num=new int(num);
//    }
//
//    ~PERSON()
//    {
//        if (m_num!=NULL)
//        {
//            delete m_num;
//            m_num = NULL;
//        }
//    }
//
//    //赋值运算符重载
//    PERSON &operator=(PERSON &p)
//    {
//        if (m_num!=NULL)
//        {
//            delete m_num;
//            m_num = NULL;
//        }
//        m_num =  new int(*p.m_num);
//        return *this;
//    }
//    int *m_num;
//};
//
//void test01()
//{
//    PERSON p(10);
//    PERSON p1(20);
//    PERSON p2(20);
//    p2=p=p1;
//    cout <<*p.m_num <<endl;
//    cout <<*p1.m_num <<endl;
//    cout <<*p2.m_num <<endl;
//}
//
//
//int main()
//{
//    test01();
//    return 0;
//}


//关系运算符重载
//class PERSON
//{
//public:
//    PERSON(string name, int num)
//    {
//        m_num=num;
//        m_name=name;
//    }
//
//    //赋值运算符重载
//    bool operator==(PERSON &p)
//    {
//        if (this->m_num==p.m_num && this->m_name==p.m_name)
//        {
//            return true;
//        }
//        return false;
//    }
//    int m_num;
//    string m_name;
//};
//
//void test01()
//{
//    PERSON p("tom",20);
//    PERSON p2("tommm",20);
//
//    if (p2==p)
//    {
//        cout << "xiandeng";
//    }
//    else
//    {
//        cout << "bubuuubuxiandeng";
//    }
//
//}
//
//
//int main()
//{
//    test01();
//    return 0;
//}


//函数调用运算符重载
class PRIENT
{

public:
    void operator()(string test)
    {
        cout << test << endl;
    }

};

class MYADD
{
public:
    int operator()(int a, int b)
    {
        return a+b;
    }
};

void test01()
{
    PRIENT myprint;
    myprint("gelloasdas");//类似函数调用，所以又称仿函数

    MYADD asd;
    int hh= asd(30,30);
    //匿名函数对象
    cout << MYADD()(10,10) <<endl;
}
int main()
{
    test01();
    return 0;
}